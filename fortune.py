import random

print("🔮 Welcome to Hansika Gupta's Fortune Teller (21JE0376) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        "✨ Your fortune: Great things await you, Hansika! Keep smiling. ✨",
        "✨ Your fortune: Happiness attracts more happiness. ✨"
    ],
    "sad": [
        "✨ Your fortune: Tough times never last, but tough people like you do. ✨",
        "✨ Your fortune: It's okay to feel sad. Brighter days are coming, Hansika. ✨"
    ],
    "neutral": [
        "✨ Your fortune: Still waters run deep—expect meaningful changes soon. ✨",
        "✨ Your fortune: Balance is a blessing. ✨"
    ],
    "stressed": [
        "✨ Your fortune: Breathe, Hansika. Clarity comes after the storm. ✨",
        "✨ Your fortune: You’re stronger than the stress you feel. ✨"
    ],
    "excited": [
        "✨ Your fortune: Ride the wave of excitement, Hansika — big things are coming! ✨",
        "✨ Your fortune: Energy is contagious. Spread your sparkle! ✨"
    ]
}

if mood in fortunes:
    print(random.choice(fortunes[mood]))
else:
    print("✨ Sorry, I can only read moods like happy, sad, neutral, stressed, or excited. ✨")
