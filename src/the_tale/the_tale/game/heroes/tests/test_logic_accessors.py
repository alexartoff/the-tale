
import smart_imports

smart_imports.all()


class HeroLogicAccessorsTestBase(utils_testcase.TestCase):

    def setUp(self):
        super(HeroLogicAccessorsTestBase, self).setUp()

        self.place_1, self.place_2, self.place_3 = game_logic.create_test_map()

        account = self.accounts_factory.create_account()

        self.storage = game_logic_storage.LogicStorage()
        self.storage.load_account_data(account.id)
        self.hero = self.storage.accounts_to_heroes[account.id]


class HeroLogicAccessorsTest(HeroLogicAccessorsTestBase):

    def check_can_process_turn(self, expected_result, banned=False, bot=False, active=False, premium=False, single=True, idle=False, sinchronized_turn=True):

        if sinchronized_turn:
            turn_number = 6 * conf.settings.INACTIVE_HERO_DELAY + self.hero.id
        else:
            turn_number = 6 * conf.settings.INACTIVE_HERO_DELAY + self.hero.id + 1

        with mock.patch('the_tale.game.heroes.objects.Hero.is_banned', banned), \
                mock.patch('the_tale.game.heroes.objects.Hero.is_bot', bot), \
                mock.patch('the_tale.game.heroes.objects.Hero.is_active', active), \
                mock.patch('the_tale.game.heroes.objects.Hero.is_premium', premium), \
                mock.patch('the_tale.game.actions.container.ActionsContainer.is_single', single), \
                mock.patch('the_tale.game.actions.container.ActionsContainer.number', 1 if idle else 2):
            self.assertEqual(self.hero.can_process_turn(turn_number), expected_result)

    def test_can_process_turn__banned(self):
        self.check_can_process_turn(True, banned=True)
        self.check_can_process_turn(False, banned=True, idle=True)
        self.check_can_process_turn(True, active=True)
        self.check_can_process_turn(True, premium=True)
        self.check_can_process_turn(True, single=False)
        self.check_can_process_turn(True, sinchronized_turn=True)
        self.check_can_process_turn(False, sinchronized_turn=False)

    def test_prefered_quest_markers__no_markers(self):
        self.assertTrue(self.hero.habit_honor.interval.is_NEUTRAL)
        self.assertTrue(self.hero.habit_peacefulness.interval.is_NEUTRAL)

        markers = set()

        for i in range(1000):
            markers |= self.hero.prefered_quest_markers()

        self.assertEqual(markers, set())

    def test_prefered_quest_markers__has_markers(self):
        self.hero.habit_honor.change(500)
        self.hero.habit_peacefulness.change(500)

        self.assertTrue(self.hero.habit_honor.interval.is_RIGHT_2)
        self.assertTrue(self.hero.habit_peacefulness.interval.is_RIGHT_2)

        markers = set()

        for i in range(1000):
            markers |= self.hero.prefered_quest_markers()

        self.hero.habit_honor.change(-1000)
        self.hero.habit_peacefulness.change(-1000)

        self.assertTrue(self.hero.habit_honor.interval.is_LEFT_2)
        self.assertTrue(self.hero.habit_peacefulness.interval.is_LEFT_2)

        for i in range(1000):
            markers |= self.hero.prefered_quest_markers()

        self.assertEqual(markers, set([questgen_relations.OPTION_MARKERS.HONORABLE,
                                       questgen_relations.OPTION_MARKERS.DISHONORABLE,
                                       questgen_relations.OPTION_MARKERS.AGGRESSIVE,
                                       questgen_relations.OPTION_MARKERS.UNAGGRESSIVE]))

    def test_update_context(self):
        additional_ability = mock.Mock()
        with mock.patch('the_tale.game.heroes.objects.Hero.abilities') as abilities:
            with mock.patch('the_tale.game.heroes.objects.Hero.additional_abilities', [additional_ability, additional_ability]):
                with mock.patch('the_tale.game.heroes.objects.Hero.habit_honor') as honor:
                    with mock.patch('the_tale.game.heroes.objects.Hero.habit_peacefulness') as peacefulness:
                        self.hero.update_context(mock.Mock(), mock.Mock())

        self.assertEqual(abilities.update_context.call_count, 1)
        self.assertEqual(additional_ability.update_context.call_count, 2)
        self.assertEqual(honor.update_context.call_count, 1)
        self.assertEqual(peacefulness.update_context.call_count, 1)

    def test_prefered_mob_loot_multiplier(self):
        self.mob = mobs_storage.mobs.get_all_mobs_for_level(level=self.hero.level)[0].create_mob(self.hero)

        self.assertEqual(self.hero.preferences.mob, None)

        with self.check_increased(lambda: self.hero.loot_probability(self.mob)):
            with self.check_increased(lambda: self.hero.artifacts_probability(self.mob)):
                self.hero.preferences.set(relations.PREFERENCE_TYPE.MOB, self.mob.record)

    def test_companion_damage__bonus_damage(self):
        companion_record = next(companions_storage.companions.enabled_companions())
        companion = companions_logic.create_companion(companion_record)
        self.hero.set_companion(companion)

        with mock.patch('the_tale.game.balance.constants.COMPANIONS_BONUS_DAMAGE_PROBABILITY', 666666):
            with mock.patch('the_tale.game.balance.constants.COMPANIONS_WOUNDS_IN_HOUR_FROM_WOUNDS', c.COMPANIONS_WOUNDS_IN_HOUR):
                with mock.patch('the_tale.game.heroes.objects.Hero.attribute_modifier', lambda s, t: 666 if t.is_COMPANION_DAMAGE else t.default()):
                    for i in range(1000):
                        self.assertEqual(self.hero.companion_damage, c.COMPANIONS_DAMAGE_PER_WOUND + 666)

    def test_companion_damage__bonus_damage__damage_from_heal(self):
        companion_record = next(companions_storage.companions.enabled_companions())
        companion = companions_logic.create_companion(companion_record)
        self.hero.set_companion(companion)

        with mock.patch('the_tale.game.balance.constants.COMPANIONS_BONUS_DAMAGE_PROBABILITY', 666666):
            with mock.patch('the_tale.game.heroes.objects.Hero.companion_damage_probability', 0):
                with mock.patch('the_tale.game.heroes.objects.Hero.attribute_modifier', lambda s, t: 666 if t.is_COMPANION_DAMAGE else t.default()):
                    for i in range(1000):
                        self.assertEqual(self.hero.companion_damage, c.COMPANIONS_DAMAGE_PER_WOUND)

    def test_companion_damage_probability(self):
        self.assertEqual(self.hero.companion_damage_probability, c.COMPANIONS_WOUND_ON_DEFEND_PROBABILITY_FROM_WOUNDS)

        with mock.patch('the_tale.game.heroes.objects.Hero.attribute_modifier', lambda s, t: 2 if t.is_COMPANION_DAMAGE_PROBABILITY else t.default()):
            self.assertEqual(self.hero.companion_damage_probability, 2)

    def test_mob_type(self):
        self.assertTrue(self.hero.mob_type.is_CIVILIZED)

    def test_communication_verbal(self):
        self.assertTrue(self.hero.communication_verbal)

    def test_communication_gestures(self):
        self.assertTrue(self.hero.communication_gestures)

    def test_communication_telepathic(self):
        with mock.patch('the_tale.game.heroes.objects.Hero.power', power.Power(0, 1)):
            self.assertTrue(self.hero.communication_telepathic.is_CAN)

        with mock.patch('the_tale.game.heroes.objects.Hero.power', power.Power(1, 0)):
            self.assertTrue(self.hero.communication_telepathic.is_CAN_NOT)

        with mock.patch('the_tale.game.heroes.objects.Hero.power', power.Power(1, 1)):
            self.assertTrue(self.hero.communication_telepathic.is_CAN_NOT)

    def test_modify_attribute(self):
        companion_record = next(companions_storage.companions.enabled_companions())
        companion = companions_logic.create_companion(companion_record)
        self.hero.set_companion(companion)

        self.assertFalse(self.hero.companion.is_dead)

        with mock.patch('the_tale.game.companions.objects.Companion.modify_attribute') as modify_attribute:
            self.hero.modify_attribute(relations.MODIFIERS.POWER, 1)

        self.assertTrue(modify_attribute.call_count >= 1)

    def test_check_attribute(self):
        companion_record = next(companions_storage.companions.enabled_companions())
        companion = companions_logic.create_companion(companion_record)
        self.hero.set_companion(companion)

        self.assertFalse(self.hero.companion.is_dead)

        with mock.patch('the_tale.game.companions.objects.Companion.check_attribute') as check_attribute:
            self.hero.check_attribute(relations.MODIFIERS.POWER)

        self.assertTrue(check_attribute.call_count >= 1)

    def test_companion_coherence_speed__no_companion(self):
        self.assertEqual(self.hero.companion_coherence_speed, 0)

    def test_companion_coherence_speed__companion_alive(self):
        companion_record = next(companions_storage.companions.enabled_companions())
        companion = companions_logic.create_companion(companion_record)
        self.hero.set_companion(companion)

        self.assertFalse(self.hero.companion.is_dead)

        self.assertGreater(self.hero.companion_coherence_speed, 0)

    def test_companion_coherence_speed__companion_dead(self):
        companion_record = next(companions_storage.companions.enabled_companions())
        companion = companions_logic.create_companion(companion_record)
        self.hero.set_companion(companion)

        self.hero.companion.health = 0
        self.assertTrue(self.hero.companion.is_dead)

        self.assertEqual(self.hero.companion_coherence_speed, 0)

    def test_keep_dead_companion(self):
        with mock.patch('the_tale.game.heroes.objects.Hero.is_premium', False):
            self.assertFalse(self.hero.keep_dead_companion())

        with mock.patch('the_tale.game.heroes.objects.Hero.is_premium', True):
            self.assertTrue(self.hero.keep_dead_companion())

    def test_is_battle_start_needed__safety(self):
        self.hero.position.cell().safety = 1.0
        self.assertTrue(all(not self.hero.is_battle_start_needed() for i in range(100)))

    @mock.patch('the_tale.game.balance.constants.MAX_BATTLES_PER_TURN', 1.0)
    def test_is_battle_start_needed__no_safety(self):
        self.hero.position.cell().safety = 0
        self.assertTrue(all(self.hero.is_battle_start_needed() for i in range(100)))

    @mock.patch('the_tale.game.heroes.objects.Hero.battles_per_turn_summand', 0.5)
    @mock.patch('the_tale.game.balance.constants.MAX_BATTLES_PER_TURN', 1.0)
    def test_is_battle_start_needed__hero_modifier(self):
        self.hero.position.cell().safety = 0.5
        self.assertTrue(all(self.hero.is_battle_start_needed() for i in range(100)))

    @mock.patch('the_tale.game.heroes.objects.Hero.battles_per_turn_summand', -0.5)
    @mock.patch('the_tale.game.balance.constants.MAX_BATTLES_PER_TURN', 1.0)
    def test_is_battle_start_needed__hero_modifier_2(self):
        self.hero.position.cell().safety = 0.5
        self.assertTrue(all(not self.hero.is_battle_start_needed() for i in range(100)))

    def test_modify_move_speed__less(self):
        self.hero.position.cell().transport = 0.5
        self.assertEqual(self.hero.modify_move_speed(10), 5)

    def test_modify_move_speed_greater(self):
        self.hero.position.cell().transport = 2.0
        self.assertEqual(self.hero.modify_move_speed(10), 20.0)


class PoliticPowerBonusTests(HeroLogicAccessorsTestBase):

    def test_banned(self):
        self.hero.might = 1000

        self.assertGreater(self.hero.politic_power_bonus(), 0)

        with mock.patch('the_tale.game.heroes.objects.Hero.is_banned', True):
            self.assertEqual(self.hero.politic_power_bonus(), 0)

    def test_bonus_below_zero(self):
        self.assertEqual(self.hero.politic_power_bonus(), 0)
        with mock.patch('the_tale.game.heroes.objects.Hero.politics_power_modifier', -666666666):
            self.assertEqual(self.hero.politic_power_bonus(), 0)

    def test_all_effects(self):
        with self.check_increased(self.hero.politic_power_bonus):
            self.hero.might = 1000

        with self.check_increased(self.hero.politic_power_bonus):
            self.hero.equipment.get(relations.EQUIPMENT_SLOT.PLATE).record.special_effect = artifacts_relations.ARTIFACT_EFFECT.GREAT_POWER

        with self.check_increased(self.hero.politic_power_bonus):
            abilities = companions_abilities_container.Container(start=(companions_abilities_effects.ABILITIES.KNOWN,))
            companion_record = companions_logic.create_random_companion_record(name='test-companion',
                                                                               state=companions_relations.STATE.ENABLED,
                                                                               abilities=abilities)
            companion = companions_logic.create_companion(companion_record)
            self.hero.set_companion(companion)

        with self.check_increased(self.hero.politic_power_bonus):
            self.hero.abilities.add(heroes_abilities_nonbattle.DIPLOMATIC.get_id(), level=5)
