from lyrics import Lyrics

text = """
His palms are sweaty, knees weak, arms are heavy
There's vomit on his sweater already, mom's spaghetti
He's nervous, but on the surface he looks calm and ready
To drop bombs, but he keeps on forgetting
What he wrote down, the whole crowd goes so loud
He opens his mouth, but the words won't come out
He's choking, how? Everybody's joking now
The clock's run out, time's up, over, blaow
Snap back to reality, ope there goes gravity, ope
There goes Rabbit, he choked, he's so mad but he won't
Give up that easy, no, he won't have it, he knows
His whole back's to these ropes, it don't matter, he's dope
He knows that but he's broke, he's so stagnant, he knows
When he goes back to this mobile home, that's when it's
Back to the lab again, yo, this old rhapsody
Better go capture this moment and hope it don't pass him, and His soul's escaping through this hole that is gaping
This world is mine for the taking, make me king
As we move toward a New World Order
A normal life is boring; but superstardom's
Close to post-mortem, it only grows harder
Homie grows hotter, he blows, it's all over
"""
song_scores = []
l = Lyrics(text=text, print_stats=False, 
            language="english")
rl = l.get_avg_rhyme_length()
print(rl)