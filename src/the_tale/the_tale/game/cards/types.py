
import smart_imports

smart_imports.all()


FOR_ALL = relations.AVAILABILITY.FOR_ALL
FOR_PREMIUMS = relations.AVAILABILITY.FOR_PREMIUMS

COMMON = relations.RARITY.COMMON
UNCOMMON = relations.RARITY.UNCOMMON
RARE = relations.RARITY.RARE
EPIC = relations.RARITY.EPIC
LEGENDARY = relations.RARITY.LEGENDARY


class CARD(rels.Relation):
    name = rels.Column(primary=True, no_index=True)
    value = rels.Column(external=True, no_index=True)
    text = rels.Column()
    availability = rels.Column(unique=False)
    rarity = rels.Column(unique=False)
    effect = rels.Column(unique=False, primary=False, single_type=False)
    combiners = rels.Column(unique=False, primary=False, single_type=False)

    records = (('ADD_BONUS_ENERGY_COMMON', 5, 'капля энергии', FOR_ALL, COMMON,
                effects.AddBonusEnergy(base=10, level=1), [reactors.Simple3()]),
               ('ADD_BONUS_ENERGY_UNCOMMON', 6, 'чаша Силы', FOR_ALL, UNCOMMON,
                effects.AddBonusEnergy(base=10, level=2), [reactors.Simple3()]),
               ('ADD_BONUS_ENERGY_RARE', 7, 'магический вихрь', FOR_ALL, RARE,
                effects.AddBonusEnergy(base=10, level=3), [reactors.Simple3()]),
               ('ADD_BONUS_ENERGY_EPIC', 8, 'энергетический шторм', FOR_ALL, EPIC,
                effects.AddBonusEnergy(base=10, level=4), [reactors.Simple3()]),
               ('ADD_BONUS_ENERGY_LEGENDARY', 9, 'шквал Силы', FOR_ALL, LEGENDARY,
                effects.AddBonusEnergy(base=10, level=5), []),

               ('ADD_GOLD_COMMON', 10, 'горсть монет', FOR_PREMIUMS, COMMON,
                effects.AddGold(base=1000, level=1), [reactors.Simple3()]),
               ('ADD_GOLD_UNCOMMON', 11, 'увесистый кошель', FOR_PREMIUMS, UNCOMMON,
                effects.AddGold(base=1000, level=2), [reactors.Simple3()]),
               ('ADD_GOLD_RARE', 12, 'сундучок на счастье', FOR_PREMIUMS, RARE,
                effects.AddGold(base=1000, level=3), [reactors.Simple3()]),

               ('CHANGE_ABILITIES_CHOICES', 39, 'альтернатива', FOR_ALL, UNCOMMON,
                effects.ChangeAbilitiesChoices(), [reactors.Special(3, 'RESET_ABILITIES')]),

               ('REPAIR_RANDOM_ARTIFACT', 45, 'фея-мастерица', FOR_ALL, UNCOMMON,
                effects.RepairRandomArtifact(), [reactors.Special(3, 'REPAIR_ALL_ARTIFACTS')]),
               ('REPAIR_ALL_ARTIFACTS', 46, 'благословение Великого Творца', FOR_ALL, RARE,
                effects.RepairAllArtifacts(), []),

               ('CANCEL_QUEST', 47, 'другие заботы', FOR_ALL, COMMON,
                effects.CancelQuest(), [reactors.Special(2, 'STOP_IDLENESS', new_cards_number=1),]),

               ('GET_ARTIFACT_COMMON', 48, 'внезапная находка', FOR_ALL, COMMON,
                effects.GetArtifact(type=0), [reactors.Simple3()]),
               ('GET_ARTIFACT_UNCOMMON', 49, 'полезный подарок', FOR_ALL, UNCOMMON,
                effects.GetArtifact(type=1), [reactors.Simple3()]),
               ('GET_ARTIFACT_RARE', 50, 'редкое приобретение', FOR_ALL, RARE,
                effects.GetArtifact(type=2), [reactors.Simple3()]),
               ('GET_ARTIFACT_EPIC', 51, 'дар Хранителя', FOR_ALL, EPIC,
                effects.GetArtifact(type=3), []),

               ('INSTANT_MONSTER_KILL', 52, 'длань Смерти', FOR_ALL, COMMON,
                effects.InstantMonsterKill(), []),

               ('KEEPERS_GOODS_COMMON', 53, 'неразменная монета', FOR_PREMIUMS, COMMON,
                effects.KeepersGoods(base=1, level=1), [reactors.Simple3()]),
               ('KEEPERS_GOODS_UNCOMMON', 54, 'волшебный горшочек', FOR_PREMIUMS, UNCOMMON,
                effects.KeepersGoods(base=1, level=2), [reactors.Simple3()]),
               ('KEEPERS_GOODS_RARE', 55, 'скатерть самобранка', FOR_PREMIUMS, RARE,
                effects.KeepersGoods(base=1, level=3), [reactors.Simple3()]),
               ('KEEPERS_GOODS_EPIC', 56, 'несметные богатства', FOR_PREMIUMS, EPIC,
                effects.KeepersGoods(base=1, level=4), [reactors.Simple3()]),
               ('KEEPERS_GOODS_LEGENDARY', 0, 'рог изобилия', FOR_PREMIUMS, LEGENDARY,
                effects.KeepersGoods(base=1, level=5), []),

               ('ADD_EXPERIENCE_COMMON', 74, 'удачная мысль', FOR_ALL, COMMON,
                effects.AddExperience(base=50, level=1), [reactors.Simple3()]),
               ('ADD_EXPERIENCE_UNCOMMON', 75, 'чистый разум', FOR_ALL, UNCOMMON,
                effects.AddExperience(base=50, level=2), [reactors.Simple3()]),
               ('ADD_EXPERIENCE_RARE', 76, 'неожиданные осложнения', FOR_ALL, RARE,
                effects.AddExperience(base=50, level=3), [reactors.Simple3()]),
               ('ADD_EXPERIENCE_EPIC', 77, 'слово Гзанзара', FOR_ALL, EPIC,
                effects.AddExperience(base=50, level=4), [reactors.Simple3()]),

               ('ADD_POWER_COMMON', 78, 'новые обстоятельства', FOR_PREMIUMS, COMMON,
                effects.AddPoliticPower(base=tt_politic_power_constants.CARD_MAX_POWER, level=5), [reactors.Simple3()]),
               ('ADD_POWER_UNCOMMON', 79, 'специальная операция', FOR_PREMIUMS, UNCOMMON,
                effects.AddPoliticPower(base=tt_politic_power_constants.CARD_MAX_POWER, level=4), [reactors.Simple3()]),
               ('ADD_POWER_RARE', 80, 'слово Дабнглана', FOR_PREMIUMS, RARE,
                effects.AddPoliticPower(base=tt_politic_power_constants.CARD_MAX_POWER, level=3), [reactors.Simple3()]),
               ('ADD_POWER_EPIC', 81, 'благословение Дабнглана', FOR_PREMIUMS, EPIC,
                effects.AddPoliticPower(base=tt_politic_power_constants.CARD_MAX_POWER, level=2), [reactors.Simple3()]),

               ('SHORT_TELEPORT', 82, 'телепорт', FOR_ALL, COMMON,
                effects.ShortTeleport(), [reactors.Special(3, 'LONG_TELEPORT')]),
               ('LONG_TELEPORT', 83, 'ТАРДИС', FOR_ALL, UNCOMMON,
                effects.LongTeleport(), []),

               ('SHARP_RANDOM_ARTIFACT', 88, 'волшебное точило', FOR_ALL, UNCOMMON,
                effects.SharpRandomArtifact(), [reactors.Special(3, 'SHARP_ALL_ARTIFACTS')]),
               ('SHARP_ALL_ARTIFACTS', 89, 'суть вещей', FOR_ALL, RARE,
                effects.SharpAllArtifacts(), []),

               ('GET_COMPANION_COMMON', 90, 'обычный спутник', FOR_ALL, COMMON,
                effects.GetCompanion(rarity=companions_relations.RARITY.COMMON), [reactors.Same2(), reactors.Simple3()]),
               ('GET_COMPANION_UNCOMMON', 91, 'необычный спутник', FOR_ALL, UNCOMMON,
                effects.GetCompanion(rarity=companions_relations.RARITY.UNCOMMON), [reactors.Same2(), reactors.Simple3()]),
               ('GET_COMPANION_RARE', 92, 'редкий спутник', FOR_ALL, RARE,
                effects.GetCompanion(rarity=companions_relations.RARITY.RARE), [reactors.Same2(), reactors.Simple3()]),
               ('GET_COMPANION_EPIC', 93, 'эпический спутник', FOR_ALL, EPIC,
                effects.GetCompanion(rarity=companions_relations.RARITY.EPIC), [reactors.Same2(), reactors.Simple3()]),
               ('GET_COMPANION_LEGENDARY', 94, 'легендарный спутник', FOR_ALL, LEGENDARY,
                 effects.GetCompanion(rarity=companions_relations.RARITY.LEGENDARY), [reactors.Same2()]),

               ('ADD_EXPERIENCE_LEGENDARY', 97, 'благословение Гзанзара', FOR_ALL, LEGENDARY,
                effects.AddExperience(base=50, level=5), []),

               ('RESET_ABILITIES', 98, 'новый путь', FOR_ALL, RARE,
                effects.ResetAbilities(), []),

               ('RELEASE_COMPANION', 99, 'четыре стороны', FOR_ALL, COMMON,
                effects.ReleaseCompanion(), [reactors.Special(3, 'FREEZE_COMPANION')]),

               ('HEAL_COMPANION_COMMON', 100, 'передышка', FOR_ALL, COMMON,
                effects.HealCompanion(base=15, level=1), [reactors.Simple3()]),
               ('HEAL_COMPANION_UNCOMMON', 101, 'подорожник', FOR_ALL, UNCOMMON,
                effects.HealCompanion(base=15, level=2), [reactors.Simple3()]),
               ('HEAL_COMPANION_RARE', 102, 'священный мёд', FOR_ALL, RARE,
                effects.HealCompanion(base=15, level=3), [reactors.Simple3()]),
               ('HEAL_COMPANION_EPIC', 103, 'молодильное яблоко', FOR_ALL, EPIC,
                effects.HealCompanion(base=15, level=4), []),

               ('INCREMENT_ARTIFACT_RARITY', 106, 'скрытый потенциал', FOR_ALL, EPIC,
                effects.UpgradeArtifact(), []),

               ('ADD_POWER_LEGENDARY', 107, 'туз в рукаве', FOR_PREMIUMS, LEGENDARY,
                effects.AddPoliticPower(base=tt_politic_power_constants.CARD_MAX_POWER, level=1), []),

               ('CHANGE_HERO_SPENDINGS', 116, 'новая цель', FOR_ALL, COMMON,
                effects.ChangeItemOfExpenditure(), [reactors.Same2()]),

               ('CHANGE_PREFERENCE', 117, 'свежий взгляд', FOR_ALL, COMMON,
                effects.ChangePreference(), [reactors.Same2()]),

               ('CHANGE_HABIT_COMMON', 118, 'сомнения', FOR_ALL, COMMON,
                effects.ChangeHabit(base=10, level=1), [reactors.Same2(), reactors.SameHabbits3(), reactors.Simple3()]),
               ('CHANGE_HABIT_UNCOMMON', 119, 'прозрение', FOR_ALL, UNCOMMON,
                effects.ChangeHabit(base=10, level=2), [reactors.Same2(), reactors.SameHabbits3(), reactors.Simple3()]),
               ('CHANGE_HABIT_RARE', 120, 'откровение', FOR_ALL, RARE,
                effects.ChangeHabit(base=10, level=3), [reactors.Same2(), reactors.SameHabbits3(), reactors.Simple3()]),
               ('CHANGE_HABIT_EPIC', 121, 'когнитивный диссонанс', FOR_ALL, EPIC,
                effects.ChangeHabit(base=10, level=4), [reactors.Same2(), reactors.SameHabbits3(), reactors.Simple3()]),
               ('CHANGE_HABIT_LEGENDARY', 122, 'экзистенциальный кризис', FOR_ALL, LEGENDARY,
                effects.ChangeHabit(base=10, level=5), [reactors.Same2()]),

               ('CREATE_CLAN', 133, 'братство', FOR_ALL, RARE,
                effects.CreateClan(), [reactors.Special(1, 'QUEST_FOR_EMISSARY', new_cards_number=9)]),

               ('ADD_GOLD_EPIC', 136, 'клад', FOR_PREMIUMS, EPIC,
                effects.AddGold(base=1000, level=4), [reactors.Simple3()]),
               ('ADD_GOLD_LEGENDARY', 137, 'фарт', FOR_PREMIUMS, LEGENDARY,
                effects.AddGold(base=1000, level=5), []),

               ('FREEZE_COMPANION', 138, 'отгул', FOR_ALL, UNCOMMON,
                effects.FreezeCompanion(), []),

               ('ADD_COMPANION_EXPERIENCE_COMMON', 139, 'наставление', FOR_ALL, COMMON,
                effects.AddCompanionExpirence(base=10, level=1), [reactors.Simple3()]),
               ('ADD_COMPANION_EXPERIENCE_UNCOMMON', 140, 'совместная тренировка', FOR_ALL, UNCOMMON,
                effects.AddCompanionExpirence(base=10, level=2), [reactors.Simple3()]),
               ('ADD_COMPANION_EXPERIENCE_RARE', 141, 'товарищество', FOR_ALL, RARE,
                effects.AddCompanionExpirence(base=10, level=3), [reactors.Simple3()]),
               ('ADD_COMPANION_EXPERIENCE_EPIC', 142, 'единство', FOR_ALL, EPIC,
                effects.AddCompanionExpirence(base=10, level=4), [reactors.Simple3()]),
               ('ADD_COMPANION_EXPERIENCE_LEGENDARY', 143, 'синхронизация', FOR_ALL, LEGENDARY,
                effects.AddCompanionExpirence(base=10, level=5), []),

               ('GIVE_COMMON_CARDS_UNCOMMON', 144, 'удачный поворот', FOR_ALL, UNCOMMON,
                effects.GiveCommonCards(base=1, level=2), [reactors.Simple3()]),
               ('GIVE_COMMON_CARDS_RARE', 145, 'колесо фортуны', FOR_ALL, RARE,
                effects.GiveCommonCards(base=1, level=3), [reactors.Simple3()]),
               ('GIVE_COMMON_CARDS_EPIC', 146, 'белая полоса', FOR_ALL, EPIC,
                effects.GiveCommonCards(base=1, level=4), [reactors.Simple3()]),
               ('GIVE_COMMON_CARDS_LEGENDARY', 147, 'прядь Кайроса', FOR_ALL, LEGENDARY,
                effects.GiveCommonCards(base=1, level=5), []),

               ('GIVE_STABILITY_UNCOMMON', 148, 'тишина', FOR_PREMIUMS, UNCOMMON,
                effects.GiveStability(base=0.01, level=1), [reactors.Simple3()]),
               ('GIVE_STABILITY_RARE', 149, 'спокойствие', FOR_PREMIUMS, RARE,
                effects.GiveStability(base=0.01, level=2), [reactors.Simple3()]),
               ('GIVE_STABILITY_EPIC', 150, 'проповедь', FOR_PREMIUMS, EPIC,
                effects.GiveStability(base=0.01, level=3), [reactors.Simple3()]),
               ('GIVE_STABILITY_LEGENDARY', 151, 'Adeptus Arbites', FOR_PREMIUMS, LEGENDARY,
                effects.GiveStability(base=0.01, level=4), []),

               ('CHANGE_HISTORY', 152, 'взмах бабочки', FOR_ALL, COMMON,
                effects.ChangeHistory(), [reactors.Same2()]),

               ('ADD_CLANS_POINTS_RARE', 153, 'дебют', FOR_PREMIUMS, RARE,
                effects.AddClansPoints(base=tt_clans_constants.TOP_CARD_POINTS_BONUS, level=3), [reactors.Simple3()]),
               ('ADD_CLANS_POINTS_EPIC', 154, 'миттельшпиль', FOR_PREMIUMS, EPIC,
                effects.AddClansPoints(base=tt_clans_constants.TOP_CARD_POINTS_BONUS, level=2), [reactors.Simple3()]),
               ('ADD_CLANS_POINTS_LEGENDARY', 155, 'эндшпиль', FOR_PREMIUMS, LEGENDARY,
                effects.AddClansPoints(base=tt_clans_constants.TOP_CARD_POINTS_BONUS, level=1), []),

                # id типа этой карты проброшен в gui объединения карт
               ('QUEST_FOR_EMISSARY', 157, 'гильдейские дела', FOR_ALL, COMMON,
                effects.QuestForEmissary(), [reactors.SameEqual2(),
                                             reactors.Special(2, 'STOP_IDLENESS', new_cards_number=1),
                                             reactors.Special(9, 'CREATE_CLAN', new_cards_number=1)]),

               ('STOP_IDLENESS', 156, 'снова в путь', FOR_ALL, COMMON,
                effects.StopIdleness(), [reactors.Special(2, 'QUEST_FOR_EMISSARY', new_cards_number=1)]),

               ('QUEST_FOR_PLACE', 158, 'общественные дела', FOR_PREMIUMS, RARE,
                effects.QuestForPlace(), [reactors.SameEqual2(),
                                          reactors.Special(3, 'QUEST_FOR_PERSON', new_cards_number=1)]),

               ('QUEST_FOR_PERSON', 159, 'личные дела', FOR_PREMIUMS, EPIC,
                effects.QuestForPerson(), [reactors.SameEqual2(),
                                           reactors.Special(1, 'QUEST_FOR_PLACE', new_cards_number=3)]),
               )


for card in CARD.records:
    for reactor in card.combiners:
        reactor.initialize(own_card_type=card)


HABIT_POINTS_CARDS = {card
                      for card in CARD.records
                      if isinstance(card.effect, effects.ChangeHabit)}
