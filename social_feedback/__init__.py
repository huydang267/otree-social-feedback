# pyre-ignore-all-errors
from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'social_feedback'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    ALL_STICKERS = [
        # Category A
        {'id': 'a1', 'path': 'social_feedback/stickers/a1_hamster_planner.png', 'cat': 'A'},
        {'id': 'a2', 'path': 'social_feedback/stickers/a2_spreadsheet_cat.png', 'cat': 'A'},
        {'id': 'a3', 'path': 'social_feedback/stickers/a3_logic_robot.png', 'cat': 'A'},
        {'id': 'a4', 'path': 'social_feedback/stickers/a4_math_coffee.png', 'cat': 'A'},
        {'id': 'a5', 'path': 'social_feedback/stickers/a5_overthinking_flowchart.png', 'cat': 'A'},
        {'id': 'a6', 'path': 'social_feedback/stickers/a6_academic_weapon.png', 'cat': 'A'},
        {'id': 'a7', 'path': 'social_feedback/stickers/a7_raccoon_sorting.png', 'cat': 'A'},
        {'id': 'a8', 'path': 'social_feedback/stickers/a8_fact_check_owl.png', 'cat': 'A'},
        {'id': 'a9', 'path': 'social_feedback/stickers/a9_master_plans.png', 'cat': 'A'},
        {'id': 'a10', 'path': 'social_feedback/stickers/a10_50_tabs.png', 'cat': 'A'},
        {'id': 'a11', 'path': 'social_feedback/stickers/a11_overthinker_trophy.png', 'cat': 'A'},
        {'id': 'a12', 'path': 'social_feedback/stickers/a12_notion_organized.png', 'cat': 'A'},
        # Category B
        {'id': 'b1', 'path': 'social_feedback/stickers/b1_daredevil_squirrel.png', 'cat': 'B'},
        {'id': 'b2', 'path': 'social_feedback/stickers/b2_fire_fox.png', 'cat': 'B'},
        {'id': 'b3', 'path': 'social_feedback/stickers/b3_yolo_graffiti.png', 'cat': 'B'},
        {'id': 'b4', 'path': 'social_feedback/stickers/b4_matchstick_impulse.png', 'cat': 'B'},
        {'id': 'b5', 'path': 'social_feedback/stickers/b5_messy_arrow.png', 'cat': 'B'},
        {'id': 'b6', 'path': 'social_feedback/stickers/b6_chaotic_luggage.png', 'cat': 'B'},
        {'id': 'b7', 'path': 'social_feedback/stickers/b7_no_thoughts_brain.png', 'cat': 'B'},
        {'id': 'b8', 'path': 'social_feedback/stickers/b8_bungee_parrot.png', 'cat': 'B'},
        {'id': 'b9', 'path': 'social_feedback/stickers/b9_delete_logic_plans.png', 'cat': 'B'},
        {'id': 'b10', 'path': 'social_feedback/stickers/b10_ignore_calls.png', 'cat': 'B'},
        {'id': 'b11', 'path': 'social_feedback/stickers/b11_risky_trophy.png', 'cat': 'B'},
        {'id': 'b12', 'path': 'social_feedback/stickers/b12_exploding_volcano.png', 'cat': 'B'},
        # Category C
        {'id': 'c1', 'path': 'social_feedback/stickers/c1_penguins_hug.png', 'cat': 'C'},
        {'id': 'c2', 'path': 'social_feedback/stickers/c2_comfort_marshmallow.png', 'cat': 'C'},
        {'id': 'c3', 'path': 'social_feedback/stickers/c3_golden_vibe_check.png', 'cat': 'C'},
        {'id': 'c4', 'path': 'social_feedback/stickers/c4_vibing_rainbow.png', 'cat': 'C'},
        {'id': 'c5', 'path': 'social_feedback/stickers/c5_dependent_flowchart.png', 'cat': 'C'},
        {'id': 'c6', 'path': 'social_feedback/stickers/c6_koala_blanket.png', 'cat': 'C'},
        {'id': 'c7', 'path': 'social_feedback/stickers/c7_jellyfish_drift.png', 'cat': 'C'},
        {'id': 'c8', 'path': 'social_feedback/stickers/c8_group_selfie.png', 'cat': 'C'},
        {'id': 'c9', 'path': 'social_feedback/stickers/c9_dreams_hearts.png', 'cat': 'C'},
        {'id': 'c10', 'path': 'social_feedback/stickers/c10_validation_like.png', 'cat': 'C'},
        {'id': 'c11', 'path': 'social_feedback/stickers/c11_peacemaker_trophy.png', 'cat': 'C'},
        {'id': 'c12', 'path': 'social_feedback/stickers/c12_sharing_boba.png', 'cat': 'C'},
    ]
    ALL_TAGLINES = [
        # Category A
        {'id': 't_a1', 'text': 'I have a spreadsheet for this.', 'cat': 'A'},
        {'id': 't_a2', 'text': 'Let me overthink this real quick.', 'cat': 'A'},
        {'id': 't_a3', 'text': 'My backup plan has a backup plan.', 'cat': 'A'},
        {'id': 't_a4', 'text': 'Academic weapon activated.', 'cat': 'A'},
        {'id': 't_a5', 'text': 'I brought the receipts.', 'cat': 'A'},
        {'id': 't_a6', 'text': 'Make it make sense.', 'cat': 'A'},
        {'id': 't_a7', 'text': 'Logic is my love language.', 'cat': 'A'},
        {'id': 't_a8', 'text': 'Data over drama.', 'cat': 'A'},
        # Category B
        {'id': 't_b1', 'text': 'Doing it for the plot.', 'cat': 'B'},
        {'id': 't_b2', 'text': 'No thoughts, just vibes.', 'cat': 'B'},
        {'id': 't_b3', 'text': "I'll figure it out on the way down.", 'cat': 'B'},
        {'id': 't_b4', 'text': 'Impulsive decisions only.', 'cat': 'B'},
        {'id': 't_b5', 'text': 'Chaos is my aesthetic.', 'cat': 'B'},
        {'id': 't_b6', 'text': 'We ball.', 'cat': 'B'},
        {'id': 't_b7', 'text': 'Risking it all for a funny story.', 'cat': 'B'},
        {'id': 't_b8', 'text': 'Full send or no send.', 'cat': 'B'},
        # Category C
        {'id': 't_c1', 'text': 'Whatever you guys want to do!', 'cat': 'C'},
        {'id': 't_c2', 'text': 'Just happy to be included.', 'cat': 'C'},
        {'id': 't_c3', 'text': 'Matching your energy.', 'cat': 'C'},
        {'id': 't_c4', 'text': 'Professional people pleaser.', 'cat': 'C'},
        {'id': 't_c5', 'text': 'I run on iced coffee and validation.', 'cat': 'C'},
        {'id': 't_c6', 'text': 'Can someone else decide, please?', 'cat': 'C'},
        {'id': 't_c7', 'text': 'Vibing and thriving together.', 'cat': 'C'},
        {'id': 't_c8', 'text': 'Designated emotional support friend.', 'cat': 'C'},
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    liked_ids = models.StringField(blank=True, initial='')

    sticker_1 = models.StringField()
    sticker_2 = models.StringField()
    sticker_3 = models.StringField()
    tagline = models.StringField()

    calculated_archetype = models.StringField()

    likes_received = models.IntegerField(initial=0)

    percentile_rank = models.IntegerField()

    is_treatment = models.BooleanField()

    boxes_collected = models.IntegerField(min=0, max=100)
    bomb_location = models.IntegerField()

    gender = models.StringField(choices=['Male', 'Female', 'Other'])
    is_econ_major = models.BooleanField(label='Are you an Economics major?')
    general_risk_tolerance = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal,
        label='On a scale from 0 to 10, how willing are you to take risks in general? (0 = Completely unwilling, 10 = Very willing)'
    )
    
    social_media_freq = models.IntegerField(
        label='How much time do you spend on social media daily?',
        choices=[
            [1, 'Rarely / Less than 1 hour'],
            [2, '1 - 2 hours'],
            [3, '2 - 4 hours'],
            [4, 'More than 4 hours']
        ],
        widget=widgets.RadioSelect
    )
    
    experiment_feedback = models.LongStringField(
        label='Do you have any thoughts, feelings, or feedback regarding this experiment?',
        blank=True
    )

    selected_for_payout = models.BooleanField(initial=False)


# PAGES
class Instructions_Part1(Page):
    pass

class Instructions_Part2(Page):
    pass

class ProfileCreation(Page):
    form_model = 'player'
    form_fields = [
        'sticker_1',
        'sticker_2',
        'sticker_3',
        'tagline',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        import random
        stickers = list(C.ALL_STICKERS)
        taglines = list(C.ALL_TAGLINES)
        random.shuffle(stickers)
        random.shuffle(taglines)
        return dict(
            ALL_STICKERS=stickers,
            ALL_TAGLINES=taglines,
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Look up categories from chosen IDs
        st_ids = [player.sticker_1, player.sticker_2, player.sticker_3]
        tg_id = player.tagline
        
        counts = {'A': 0, 'B': 0, 'C': 0}
        
        # Tally sticker categories
        for s in C.ALL_STICKERS:
            if s['id'] in st_ids:
                counts[s['cat']] += 1
                
        # Tally tagline category and record tie-breaker
        tag_cat = 'A' # Default fallback
        for t in C.ALL_TAGLINES:
            if t['id'] == tg_id:
                tag_cat = t['cat']
                counts[tag_cat] += 1

        max_count = max(counts.values())
        winners = [k for k, v in counts.items() if v == max_count]

        # Tie breaker: defaults to tagline's category if tie
        if len(winners) > 1:
            winner = tag_cat
        else:
            winner = winners[0]

        archetype_map = {
            'A': 'The Calculated Strategist',
            'B': 'The Bold Adventurer',
            'C': 'The Social Harmonizer'
        }

        player.calculated_archetype = archetype_map.get(winner)


class VotingWaitPage(WaitPage):
    pass

class PeerVoting(Page):
    form_model = 'player'
    form_fields = ['liked_ids']

    @staticmethod
    def vars_for_template(player: Player):
        other_players = player.get_others_in_subsession()
        return dict(
            other_players=other_players,
            ALL_STICKERS=C.ALL_STICKERS,
            ALL_TAGLINES=C.ALL_TAGLINES,
        )

class CalculationWaitPage(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        players = subsession.get_players()
        import random
        
        # Tally aggregate likes
        for p in players:
            if p.liked_ids:
                liked_list = p.liked_ids.split(',')
                for lid in liked_list:
                    lid = lid.strip()
                    if lid.isdigit():
                        target = None
                        for p_itr in players:
                            if p_itr.id_in_group == int(lid):
                                target = p_itr
                                break
                        if target:
                            target.likes_received += 1
                            
        # Calculate percentile logic
        # Because we're in oTree 5+, sorting relies on `p.likes_received`
        sorted_likes = sorted([p.likes_received for p in players], reverse=True)
        for p in players:
            # 0 index rank
            rank = sorted_likes.index(p.likes_received)
            top_pct = max(1, int((rank / len(players)) * 100))
            p.percentile_rank = int(round(top_pct))
            
        # Isolate exactly 50% randomly for treatment
        # (Handling odd lists by flooring)
        treatment_players = random.sample(players, len(players) // 2)
        for p in players:
            p.is_treatment = (p in treatment_players)

class TreatmentFeedback(Page):
    pass

class BRET_Task(Page):
    form_model = 'player'
    form_fields = ['boxes_collected']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random
        # Randomly assign bomb location between 1 and 100
        player.bomb_location = random.randint(1, 100)

class PostSurvey(Page):
    form_model = 'player'
    form_fields = ['gender', 'is_econ_major', 'general_risk_tolerance', 'social_media_freq', 'experiment_feedback']

class FinalWaitPage(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        players = subsession.get_players()
        import random

        # Randomly select exactly 1 player
        winner = random.choice(players)

        for p in players:
            if p == winner:
                p.selected_for_payout = True
                
                # Calculate payoff based on $0.20 per box
                if p.bomb_location <= p.boxes_collected:
                    p.payoff = 0
                else:
                    p.payoff = float(p.boxes_collected) * 0.20
            else:
                p.selected_for_payout = False
                p.payoff = 0

class Results(Page):
    pass

page_sequence = [
    Instructions_Part1,
    Instructions_Part2,
    ProfileCreation, 
    VotingWaitPage, 
    PeerVoting, 
    CalculationWaitPage, 
    TreatmentFeedback, 
    BRET_Task,
    PostSurvey,
    FinalWaitPage,
    Results
]
