import random

fortunes = ['Circumstance does not make a man; it reveals him to himself', 'Sing and rejoice, fortune is smiling on you','It is much easier to look for the bad, than it is to find the good','You will make many changes before settling down happily','Be assertive when decisive action is needed','A clear conscience is usually a sign of a bad memory','Never give up...unless someone pays you a lot of money to do so','Ignore previous fortunes','Never trust a cookie for advice','Hearty laughter is a good way to jog internally without having to go outdoors','The fortune you seek is in another cookie','Some fortune cookies contain no fortune','Every exit is an entrance to new experiences','You will be hungry again in one hour','You are not illiterate','Your smile will tell you what makes you feel good','Your reality check is about to bounce',"It's okay to look at the past and future. Just don't stare",'He who dies with most toys, still dies','Life is a sexually transmitted condition',"I cannot help you, for I'm just a cookie",'If you do not want someone to ask you to do something again, do it terribly the first time','If you are not happy where you are, move. You are not a tree',"When you need to borrow money, borrow from a pessimist. They won't expect it back",'You will get everything you want in life if you lower your expectations','Never test the depth of a river with both feet','Silence is golden, but duct tape is silver','Put some prance in your dance',"Don't be that guy",'Do not protect yourseld by a fence, but rather by your friends','The heart that loves is always young','Fall seven times, stand up eight','Do not think there are no crocodiles because the water is calm','It is impossible to awaken someone who is pretending to sleep','Not to know is bad; not wish to know is worse','Do not throw away the old bucket until you know whether the new one holds water','Go often to the house of a friend; for weeds soon choke up the unused path','Shared joy is a double joy; shared sorrow is half a sorrow']

random.shuffle(fortunes)

print random.choice(fortunes) + " " + "*" "Your lucky numbers are:" + str(random.sample(range(1,100), 4)) + "*"




