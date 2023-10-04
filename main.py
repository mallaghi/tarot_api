from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

cards = {
    'fool': {
        'id' : 1,
        'meaning': 'Embrace new beginnings and spontaneity with the Fool. This card represents untapped potential and the joy of exploration.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/RWS_Tarot_00_Fool.jpg/309px-RWS_Tarot_00_Fool.jpg',
    },
    'magician': {
        'id' : 2,
        'meaning': 'Manifest your desires and showcase resourcefulness with the Magician. This card symbolizes the power to turn dreams into reality.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/RWS_Tarot_01_Magician.jpg/136px-RWS_Tarot_01_Magician.jpg',
    },
    'high_priestess': {
        'id' : 3,
        'meaning': 'Trust your intuition and explore hidden knowledge with the High Priestess. Embrace the mysteries within and connect with your subconscious.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/RWS_Tarot_02_High_Priestess.jpg/311px-RWS_Tarot_02_High_Priestess.jpg',
    },
    'emperor': {
        'id' : 4,
        'meaning': 'Establish stability and leadership with the Emperor. This card signifies authority and the wisdom to build a strong foundation for success.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/c/c3/RWS_Tarot_04_Emperor.jpg',
    },
    'lovers': {
        'id' : 5,
        'meaning': 'Experience deep connections and make heart-centered choices with the Lovers. Embrace harmony, love, and partnerships.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/3/3a/TheLovers.jpg',
    },
    'chariot': {
        'id' : 6,
        'meaning': 'Triumph over challenges and balance opposing forces with the Chariot. Move forward with determination and focus on victory.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/RWS_Tarot_07_Chariot.jpg/136px-RWS_Tarot_07_Chariot.jpg',
    },
    'justice': {
        'id' : 7,
        'meaning': 'Act with integrity and trust in karmic balance with Justice. This card symbolizes fairness, truth, and the consequences of your actions.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/RWS_Tarot_11_Justice.jpg/138px-RWS_Tarot_11_Justice.jpg',
    },
    'hermit': {
        'id' : 8,
        'meaning': 'Embark on a journey of introspection and inner guidance with the Hermit. Seek answers within and discover your own inner light.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/RWS_Tarot_09_Hermit.jpg/137px-RWS_Tarot_09_Hermit.jpg',
    },
    'wheel_of_fortune': {
        'id' : 9,
        'meaning': 'Embrace the cycles of life and destiny with the Wheel of Fortune. This card signifies change, luck, and the inevitable turning of the cosmic wheel.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/RWS_Tarot_10_Wheel_of_Fortune.jpg/139px-RWS_Tarot_10_Wheel_of_Fortune.jpg',
    },
    'strength': {
        'id' : 10,
        'meaning': 'Harness inner strength and resilience with the Strength card. Face challenges with courage and gentleness, knowing that true power comes from within.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/RWS_Tarot_08_Strength.jpg/133px-RWS_Tarot_08_Strength.jpg',
    },
    'hanged_man': {
        'id' : 11,
        'meaning': 'Surrender and gain a new perspective with the Hanged Man. This card symbolizes sacrifice, release, and a profound shift in perception.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/RWS_Tarot_12_Hanged_Man.jpg/136px-RWS_Tarot_12_Hanged_Man.jpg',
    },
    'death': {
        'id' : 12,
        'meaning': 'Embrace transformation and new beginnings with the Death card. This represents the end of one chapter and the start of another, bringing renewal and rebirth.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/RWS_Tarot_13_Death.jpg/136px-RWS_Tarot_13_Death.jpg',
    },
    'temperance': {
        'id' : 13,
        'meaning': 'Find balance and harmony in all aspects of life with Temperance. This card signifies moderation, patience, and the blending of opposites.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/RWS_Tarot_14_Temperance.jpg/138px-RWS_Tarot_14_Temperance.jpg',
    },
    'devil': {
        'id' : 14,
        'meaning': 'Confront and release limiting beliefs with the Devil. This card represents temptation, bondage, and the opportunity to break free from self-imposed chains.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/RWS_Tarot_15_Devil.jpg/137px-RWS_Tarot_15_Devil.jpg',
    },
    'tower': {
        'id' : 15,
        'meaning': 'Embrace sudden change and revelation with the Tower. This card signifies upheaval, breaking down old structures, and the potential for a powerful awakening.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/RWS_Tarot_16_Tower.jpg/140px-RWS_Tarot_16_Tower.jpg',
    },
    'star': {
        'id' : 16,
        'meaning': 'Find hope, inspiration, and guidance with the Star. This card represents optimism, spiritual insight, and the fulfillment of dreams.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/RWS_Tarot_17_Star.jpg/139px-RWS_Tarot_17_Star.jpg',
    },
    'moon': {
        'id' : 17,
        'meaning': 'Navigate the mysteries of the subconscious mind with the Moon. This card symbolizes intuition, dreams, and the exploration of hidden realms.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/RWS_Tarot_18_Moon.jpg/136px-RWS_Tarot_18_Moon.jpg',
    },
    'sun': {
        'id' : 18,
        'meaning': 'Bask in the joy, vitality, and clarity of the Sun. This card represents success, enlightenment, and the radiant energy of positive transformation.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/RWS_Tarot_19_Sun.jpg/139px-RWS_Tarot_19_Sun.jpg',
    },
    'judgement': {
        'id' : 19,
        'meaning': 'Experience spiritual awakening and rebirth with Judgement. This card signifies self-discovery, accountability, and the call to embrace your true purpose.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/RWS_Tarot_20_Judgement.jpg/139px-RWS_Tarot_20_Judgement.jpg',
    },
    'world': {
        'id' : 20,
        'meaning': 'Celebrate completion and fulfillment with the World. This card symbolizes achievement, wholeness, and the successful conclusion of a significant journey.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/RWS_Tarot_21_World.jpg/137px-RWS_Tarot_21_World.jpg',
    },
    'ace_of_wands': {
        'id' : 21,
        'meaning': 'Ignite new creative ventures and passion with the Ace of Wands. This card symbolizes inspiration, potential, and the spark of a bold idea.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Wands01.jpg/137px-Wands01.jpg'
    },
    'two_of_wands': {
        'id' : 22,
        'meaning': 'Embark on a journey of decision-making and planning with the Two of Wands. This card signifies foresight, discovery, and the exploration of possibilities.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Wands02.jpg/138px-Wands02.jpg',
    },
    'three_of_wands': {
        'id' : 23,
        'meaning': 'Expand your horizons and embrace new opportunities with the Three of Wands. This card represents foresight, leadership, and the anticipation of success.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wands03.jpg/136px-Wands03.jpg',
    },
    'four_of_wands': {
        'id' : 24,
        'meaning': 'Celebrate achievements and stability with the Four of Wands. This card symbolizes harmony, community, and the joy of shared success.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Wands04.jpg/136px-Wands04.jpg',
    },
    'five_of_wands': {
        'id' : 25,
        'meaning': 'Navigate through conflicts and competition with the Five of Wands. This card encourages adaptability, teamwork, and finding common ground.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Wands05.jpg/137px-Wands05.jpg',
    },
    'six_of_wands': {
        'id' : 26,
        'meaning': 'Achieve recognition and victory with the Six of Wands. This card symbolizes public acclaim, success, and the acknowledgment of your efforts by others.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Wands06.jpg/138px-Wands06.jpg',
    },
    'seven_of_wands': {
        'id' : 27,
        'meaning': 'Stand your ground and face challenges with the Seven of Wands. This card represents courage, resilience, and the strength to defend your position.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wands07.jpg/136px-Wands07.jpg',
    },
    'eight_of_wands': {
        'id' : 28,
        'meaning': 'Experience swift and dynamic progress with the Eight of Wands. This card signifies quick communication, travel, and the manifestation of your desires.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Wands08.jpg/136px-Wands08.jpg',
    },
    'nine_of_wands': {
        'id' : 29,
        'meaning': 'Persevere through challenges and demonstrate resilience with the Nine of Wands. This card symbolizes determination, courage, and the strength to keep going.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Tarot_Nine_of_Wands.jpg/138px-Tarot_Nine_of_Wands.jpg',
    },
    'ten_of_wands': {
        'id' : 30,
        'meaning': 'Navigate the burdens of responsibility and completion with the Ten of Wands. This card represents the fulfillment of tasks, the weight of success, and the need to delegate.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Wands10.jpg/139px-Wands10.jpg',
    },
    'page_of_wands': {
        'id' : 31,
        'meaning': 'Embrace a new phase of inspiration and exploration with the Page of Wands. This card signifies youthful energy, curiosity, and the pursuit of creative endeavors.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Wands11.jpg/136px-Wands11.jpg',
    },
    'knight_of_wands': {
        'id' : 32,
        'meaning': 'Embark on a daring adventure and pursue your goals with the Knight of Wands. This card represents passion, impulsiveness, and the boldness to chase your dreams.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Wands12.jpg/136px-Wands12.jpg',
    },
    'queen_of_wands': {
        'id' : 33,
        'meaning': 'Embody confidence, charisma, and leadership with the Queen of Wands. This card symbolizes a nurturing spirit, creativity, and the ability to inspire others.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Wands13.jpg/137px-Wands13.jpg',
    },
    'king_of_wands': {
        'id' : 34,
        'meaning': 'Harness your leadership qualities and visionary spirit with the King of Wands. This card represents mastery, inspiration, and the ability to turn creative ideas into reality.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Wands14.jpg/135px-Wands14.jpg',
    },
    'ace_of_pentacles': {
        'id' : 35,
        'meaning': 'Embrace new financial and material opportunities with the Ace of Pentacles. This card signifies prosperity, abundance, and the potential for material success.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Pents01.jpg/137px-Pents01.jpg',
    },
    'two_of_pentacles': {
        'id' : 36,
        'meaning': 'Balance financial and practical matters with the Two of Pentacles. This card represents adaptability, juggling responsibilities, and finding harmony in dual pursuits.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Pents02.jpg/138px-Pents02.jpg',
    },
    'three_of_pentacles': {
        'id' : 37,
        'meaning': 'Collaborate and showcase your skills with the Three of Pentacles. This card signifies teamwork, craftsmanship, and the recognition of your expertise.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/42/Pents03.jpg',
    },
    'four_of_pentacles': {
        'id' : 38,
        'meaning': 'Evaluate your relationship with material possessions and security with the Four of Pentacles. This card represents financial stability, but also the need to avoid excessive attachment.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Pents04.jpg/136px-Pents04.jpg',
    },
    'five_of_pentacles': {
        'id' : 39,
        'meaning': 'Navigate through financial challenges and seek support with the Five of Pentacles. This card represents resilience, resourcefulness, and the strength to overcome difficulties.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Pents05.jpg/137px-Pents05.jpg',
    },
    'six_of_pentacles': {
        'id' : 40,
        'meaning': 'Experience generosity and share your wealth with the Six of Pentacles. This card signifies charity, financial assistance, and the balanced exchange of resources.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Pents06.jpg/138px-Pents06.jpg',
    },
    'seven_of_pentacles': {
        'id' : 41,
        'meaning': 'Reevaluate your long-term goals and investments with the Seven of Pentacles. This card represents patience, assessment, and the anticipation of future rewards.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Pents07.jpg/136px-Pents07.jpg',
    },
    'eight_of_pentacles': {
        'id' : 42,
        'meaning': 'Dedicate yourself to mastering your craft and honing your skills with the Eight of Pentacles. This card signifies diligence, craftsmanship, and the pursuit of excellence.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Pents08.jpg/137px-Pents08.jpg',
    },
    'nine_of_pentacles': {
        'id' : 43,
        'meaning': 'Enjoy the fruits of your labor and savor financial independence with the Nine of Pentacles. This card represents self-sufficiency, luxury, and the rewards of hard work.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/f/f0/Pents09.jpg',
    },
    'ten_of_pentacles': {
        'id' : 44,
        'meaning': 'Celebrate prosperity, wealth, and family legacy with the Ten of Pentacles. This card signifies financial security, generational wealth, and the fulfillment of long-term goals.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/42/Pents10.jpg',
    },
    'page_of_pentacles': {
        'id' : 45,
        'meaning': 'Embark on a journey of practical learning and financial exploration with the Page of Pentacles. This card signifies curiosity, studiousness, and the pursuit of tangible goals.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Pents11.jpg',
    },
    'knight_of_pentacles': {
        'id' : 46,
        'meaning': 'Approach tasks with dedication, reliability, and attention to detail with the Knight of Pentacles. This card represents a steady and methodical approach to achieving goals.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/d/d5/Pents12.jpg',
    },
    'queen_of_pentacles': {
        'id' : 47,
        'meaning': 'Embody practicality, nurturing, and financial wisdom with the Queen of Pentacles. This card symbolizes a grounded and nurturing approach to material and familial matters.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/8/88/Pents13.jpg',
    },
    'king_of_pentacles': {
        'id' : 48,
        'meaning': 'Lead with stability, abundance, and financial mastery with the King of Pentacles. This card represents success, responsibility, and the ability to manifest prosperity.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/1/1c/Pents14.jpg',
    },
    'ace_of_swords': {
        'id' : 49,
        'meaning': 'Embrace clarity, truth, and mental breakthroughs with the Ace of Swords. This card signifies triumph over adversity and the power of a sharp, focused mind.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Swords01.jpg/137px-Swords01.jpg',
    },
    'two_of_swords': {
        'id' : 50,
        'meaning': 'Confront difficult decisions and find balance with the Two of Swords. This card represents a temporary standstill, the need for introspection, and the search for equilibrium.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Swords02.jpg/138px-Swords02.jpg',
    },
    'three_of_swords': {
        'id' : 51,
        'meaning': 'Navigate through heartbreak and emotional pain with the Three of Swords. This card signifies sorrow, healing, and the importance of facing and processing emotional wounds.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Swords03.jpg/135px-Swords03.jpg',
    },
    'four_of_swords': {
        'id' : 52,
        'meaning': 'Take a moment of rest, reflection, and recovery with the Four of Swords. This card represents healing, recuperation, and the restoration of mental and physical energy.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Swords04.jpg/135px-Swords04.jpg',
    },
    'five_of_swords': {
        'id' : 53,
        'meaning': 'Navigate through conflicts and choose your battles wisely with the Five of Swords. This card signifies victory with a cost, the importance of strategy, and the need to avoid unnecessary confrontations.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Swords05.jpg/136px-Swords05.jpg',
    },
    'six_of_swords': {
        'id' : 54,
        'meaning': 'Move towards a calmer, more stable future with the Six of Swords. This card represents transition, mental clarity, and the journey from turbulence to smoother waters.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Swords06.jpg/139px-Swords06.jpg',
    },
    'seven_of_swords': {
        'id' : 55,
        'meaning': 'Navigate through deception and strategize with the Seven of Swords. This card signifies the importance of planning, cunning, and the potential for unexpected challenges.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Swords07.jpg/138px-Swords07.jpg',
    },
    'eight_of_swords': {
        'id' : 56,
        'meaning': 'Confront self-imposed limitations and find a way forward with the Eight of Swords. This card represents the power to break free from mental constraints and regain perspective.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Swords08.jpg/139px-Swords08.jpg',
    },
    'nine_of_swords': {
        'id' : 57,
        'meaning': 'Address anxiety and fear with the Nine of Swords. This card signifies inner turmoil, nightmares, and the importance of seeking support to overcome mental distress.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Swords09.jpg/138px-Swords09.jpg',
    },
    'ten_of_swords': {
        'id' : 58,
        'meaning': 'Embrace the end of a challenging cycle and the dawn of a new beginning with the Ten of Swords. This card signifies closure, transformation, and the potential for renewal after a difficult period.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Swords10.jpg/139px-Swords10.jpg',
    },
    'page_of_swords': {
        'id' : 59,
        'meaning': 'Embark on a journey of intellectual curiosity and communication with the Page of Swords. This card signifies youthful energy, curiosity, and the pursuit of truth and knowledge.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Swords11.jpg/137px-Swords11.jpg',
    },
    'knight_of_swords': {
        'id' : 60,
        'meaning': 'Pursue your goals with determination, focus, and swift action with the Knight of Swords. This card represents a fearless approach to challenges and the pursuit of justice.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Swords12.jpg/137px-Swords12.jpg',
    },
    'queen_of_swords': {
        'id' : 61,
        'meaning': 'Embody intellect, independence, and clear communication with the Queen of Swords. This card symbolizes a sharp mind, resilience, and the ability to make decisions with clarity.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Swords13.jpg/134px-Swords13.jpg',
    },
    'king_of_swords': {
        'id' : 62,
        'meaning': 'Lead with authority, intellectual mastery, and fair judgment with the King of Swords. This card represents the power of clear communication, logic, and the pursuit of truth.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Swords14.jpg/137px-Swords14.jpg',
    },
    'ace_of_cups': {
        'id' : 63,
        'meaning': 'Embrace emotional and spiritual new beginnings with the Ace of Cups. This card signifies love, intuition, and the potential for deep emotional fulfillment.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/3/36/Cups01.jpg',
    },
    'two_of_cups': {
        'id' : 64,
        'meaning': 'Celebrate partnerships and emotional connections with the Two of Cups. This card represents harmony, mutual respect, and the power of shared emotions.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/f/f8/Cups02.jpg',
    },
    'three_of_cups': {
        'id' : 65,
        'meaning': 'Revel in joyful gatherings, friendship, and celebrations with the Three of Cups. This card signifies shared happiness, connection, and the importance of expressing gratitude.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/7/7a/Cups03.jpg',
    },
    'four_of_cups': {
        'id' : 66,
        'meaning': 'Reflect on emotional fulfillment and seek inner contentment with the Four of Cups. This card represents contemplation, introspection, and the potential for new perspectives.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Cups04.jpg',
    },
    'five_of_cups': {
        'id' : 67,
        'meaning': 'Navigate through emotional loss and find healing with the Five of Cups. This card signifies grief, acceptance, and the importance of focusing on what can be salvaged.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/d/d7/Cups05.jpg',
    },
    'six_of_cups': {
        'id' : 68,
        'meaning': 'Embrace nostalgia, innocence, and joyful memories with the Six of Cups. This card signifies the return of past influences, childhood joy, and the power of sentimental connections.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/1/17/Cups06.jpg',
    },
    'seven_of_cups': {
        'id' : 69,
        'meaning': 'Confront choices, dreams, and illusions with the Seven of Cups. This card signifies imagination, fantasy, and the importance of discerning reality from illusion.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Cups07.jpg',
    },
    'eight_of_cups': {
        'id' : 70,
        'meaning': 'Embark on a journey of emotional growth and self-discovery with the Eight of Cups. This card represents the pursuit of deeper meaning, leaving behind what no longer serves, and the quest for inner fulfillment.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Cups08.jpg/137px-Cups08.jpg',
    },
    'nine_of_cups': {
         'id' : 71,
        'meaning': 'Experience emotional satisfaction and fulfillment with the Nine of Cups. This card signifies contentment, joy, and the realization of heartfelt desires.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Cups09.jpg/136px-Cups09.jpg',
    },
    'ten_of_cups': {
         'id' : 72,
        'meaning': 'Celebrate harmonious relationships, emotional fulfillment, and domestic bliss with the Ten of Cups. This card represents joyous connections, love, and the attainment of emotional abundance.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Cups10.jpg/136px-Cups10.jpg',
    },
    'page_of_cups': {
         'id' : 73,
        'meaning': 'Embark on a journey of emotional exploration and creative expression with the Page of Cups. This card signifies intuition, sensitivity, and the pursuit of imaginative endeavors.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Cups11.jpg/134px-Cups11.jpg',
    },
    'knight_of_cups': {
         'id' : 74,
        'meaning': 'Pursue your dreams with romanticism, creativity, and emotional depth with the Knight of Cups. This card represents a quest for inspiration, artistic expression, and the pursuit of love.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Cups12.jpg',
    },
    'queen_of_cups': {
         'id' : 75,
        'meaning': 'Embody compassion, intuition, and emotional understanding with the Queen of Cups. This card symbolizes emotional maturity, empathy, and the nurturing of others.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/6/62/Cups13.jpg',
    },
    'king_of_cups': {
         'id' : 76,
        'meaning': 'Lead with emotional intelligence, empathy, and calm authority with the King of Cups. This card represents mastery of emotions, compassionate leadership, and the ability to navigate complex feelings.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Cups14.jpg/136px-Cups14.jpg',
    },
     'empress': {
        'id' : 77,
        'meaning': 'Nurture creativity, fertility, and abundance with the Empress. This card symbolizes the power of nurturing, growth, and the manifestation of ideas into reality.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/d/d2/RWS_Tarot_03_Empress.jpg',
    },
    'hierophant': {
        'id' : 78,
        'meaning': 'Seek spiritual guidance, tradition, and wisdom with the Hierophant. This card represents a connection to higher principles, religious beliefs, and the importance of tradition.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/RWS_Tarot_05_Hierophant.jpg/137px-RWS_Tarot_05_Hierophant.jpg',
    },
}

class TarotCards(Resource):
    def get(self, card=None):
        if card:
            if card in cards:
                return cards[card]
            else:
                return {"error": "Card not found"}, 404
        else:
            return cards






api.add_resource(TarotCards, "/","/tarotcards/<string:card>")



# @app.route('/get-card/<card_id>')
# def get_card(card_id):
#     tarot_cards = {
#         "card_id" : card_id,
#         "name" : 'The Sun'

#           }
#     extra = request.args.get('extra')
#     if extra:
#         tarot_cards["extra"] = extra
#     return jsonify(tarot_cards), 200

if __name__ == "__main__":
    app.run(port=8000, debug=True)
