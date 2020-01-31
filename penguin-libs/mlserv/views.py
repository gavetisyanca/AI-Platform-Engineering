from flask import render_template, request
from mlserv import app
from random import randint
from mlserv.models.ML_stack_ensemble import *
from mlserv.helpers import *
import preprocessing

model = Model()
preprocessing = preprocessing

### Constants
stars = [1,5,5,5,1,4,3,1,2,3]
reviews = [
    'Total bill for this horrible service? Over $8Gs. These crooks actually had the nerve to charge us $69 for 3 pills. I checked online the pills can be had for 19 cents EACH! Avoid Hospital ERs at all costs.',
    'I *adore* Travis at the Hard Rock\'s new Kelly Cardenas Salon!  I\'m always a fan of a great blowout and no stranger to the chains that offer this service; however, Travis has taken the flawless blowout to a whole new level!  <br /><br />Travis\'s greets you with his perfectly green swoosh in his otherwise perfectly styled black hair and a Vegas-worthy rockstar outfit.  Next comes the most relaxing and incredible shampoo -- where you get a full head message that could cure even the very worst migraine in minutes --- and the scented shampoo room.  Travis has freakishly strong fingers (in a good way) and use the perfect amount of pressure.  That was superb!  Then starts the glorious blowout... where not one, not two, but THREE people were involved in doing the best round-brush action my hair has ever seen.  The team of stylists clearly gets along extremely well, as it\'s evident from the way they talk to and help one another that it\'s really genuine and not some corporate requirement.  It was so much fun to be there! <br /><br />Next Travis started with the flat iron.  The way he flipped his wrist to get volume all around without over-doing it and making me look like a Texas pagent girl was admirable.  It\'s also worth noting that he didn\'t fry my hair -- something that I\'ve had happen before with less skilled stylists.  At the end of the blowout & style my hair was perfectly bouncey and looked terrific.  The only thing better?  That this awesome blowout lasted for days! <br /><br />Travis, I will see you every single time I\'m out in Vegas.  You make me feel beauuuutiful!',
    'I have to say that this office really has it together, they are so organized and friendly!  Dr. J. Phillipp is a great dentist, very friendly and professional.  The dental assistants that helped in my procedure were amazing, Jewel and Bailey helped me to feel comfortable!  I don\'t have dental insurance, but they have this insurance through their office you can purchase for $80 something a year and this gave me 25% off all of my dental work, plus they helped me get signed up for care credit which I knew nothing about before this visit!  I highly recommend this office for the nice synergy the whole office has!',
    'Went in for a lunch. Steak sandwich was delicious, and the Caesar salad had an absolutely delicious dressing, with a perfect amount of dressing, and distributed perfectly across each leaf. I know I\'m going on about the salad ... But it was perfect.<br /><br />Drink prices were pretty good.<br /><br />The Server, Dawn, was friendly and accommodating. Very happy with her.<br /><br />In summation, a great pub experience. Would go again!',
    'Today was my second out of three sessions I had paid for. Although my first session went well, I could tell Meredith had a particular enjoyment for her male clients over her female. However, I returned because she did my teeth fine and I was pleased with the results. When I went in today, I was in the whitening room with three other gentlemen. My appointment started out well, although, being a person who is in the service industry, I always attend to my female clientele first when a couple arrives. Unbothered by those signs, I waited my turn. She checked on me once after my original 30 minute timer to ask if I was ok. She attended my boyfriend on numerous occasions, as well as the other men, and would exit the room without even asking me or looking to see if I had any irritation. Half way through, another woman had showed up who she was explaining the deals to in the lobby. While she admits timers must be reset half way through the process, she reset my boyfriends, left, rest the gentleman furthest away from me who had time to come in, redeem his deal, get set, and gave his timer done, before me, then left, and at this point my time was at 10 minutes. So, she should have reset it 5 minutes ago, according to her. While I sat there patiently this whole time with major pain in my gums, i watched the time until the lamp shut off. Not only had she reset two others, explained deals to other guest, but she never once checked on my time. When my light turned off, I released the stance of my mouth to a more relaxed state, assuming I was only getting a thirty minute session instead of the usual 45, because she had yet to come in. At this point, the teeth formula was not only burning the gum she neglected for 25 minutes now, but it began to burn my lips. I began squealing and slapping my chair trying to get her attention from the other room in a panic. I was in so much pain, that by the time she entered the room I was already out of my chair. She finally then acknowledged me, and asked if she could put vitamin E on my gum burn (pictured below). At this point, she has treated two other gums burns, while neglecting me, and I was so irritated that I had to suffer, all I wanted was to leave. While I waited for my boyfriend, she kept harassing me about the issue. Saying, \"well burns come with teeth whitening.\" While I totally agree, and under justifiable circumstances would not be as irritate, it could have easily been avoid if she had checked on me even a second time, so I could let her know. Not only did she never check on my physical health, she couldn\'t even take two seconds to reset the timer, which she even admitted to me. Her accuse was that she was coming in to do it, but I had the light off for a solid two minutes before I couldn\'t stand the pain. She admitted it should be reset every 15 minutes, which means for 25 minutes she did not bother to help me at all. Her guest in the lobby then proceeded to attack me as well, simply because I wanted to leave after the way I was treated. I also expected a refund for not getting a complete session today, due to the neglect, and the fact I won\'t be returning for my last, she had failed to do that. She was even screaming from the door, and continued to until my boyfriend and I were down the steps. I have never in my life been more appalled by a grown woman\'s behavior, who claims to be in the business for \"10 years.\" Admit your wrongs, but don\'t make your guest feel unwelcome because you can\'t do you job properly.',
    'I\'ll be the first to admit that I was not excited about going to La Tavolta. Being a food snob, when a group of friends suggested we go for dinner I looked online at the menu and to me there was nothing special and it seemed overpriced.  Im also not big on ordering pasta when I go out. Alas, I was outnumbered. Thank goodness! I ordered the sea bass special. It was to die for. Cooked perfectly, seasoned perfectly, perfect portion. I can not say enough good things about this dish. When the server asked how it was he seemed very proud of the dish and said, \" doesn\'t she (the chef) do an incredible job?\" She does. <br /><br />My hubby got the crab tortellini and also loved his. I heard \"mmmm this is so good\" from all around the table. Our waiter was super nice and even gave us free desserts because we were some of the last people in the restaurant. Service was very slow and the place was PACKED but we had our jugs of wine and a large group with good conversation so it didn\'t seem to bother anyone.<br /><br />So-<br /><br />Do order the calamari and fried zucchini appetizers. Leave out the mussels. <br /><br />If they have the sea bass special, I highly recommend it. The chicken parm and crab tortellini were also very good and very big. The chicken Romano was a bit bland. The house salads were teeny. <br /><br />Do make a reservation but still expect to wait for your food. Go with a large group of people and plan for it to be loud. Don\'t go with a date unless you\'re fighting and don\'t feel like hearing anything they have to say.  Ask to sit in the side room if it\'s available.',
    'Tracy dessert had a big name in Hong Kong and the one in First Markham place has been here for many years now! <br /><br />Came in for some Chinese dessert, and I must say their selection has increased tremendously over the years. I might as well add that the price has also increased tremendously as well. The waitress gave us tea, which I could taste had red date in it. Fancy!<br /><br />A simple taro with coconut with tapioca pearls was like $5.25 or something. Basically all the desserts were more than $5. That\'s crazy! I can literally just make this dessert at home and for a bowl, it would probably cost like $0.50. A few years ago, I think I can still get it for like $3-$4, which is more reasonable, but wow, more than $5 is a little over the top for this dessert. Though I must say, it is Tracy Dessert, and they are a little more on the expensive side. <br /><br />I also saw other items on the menu like fish balls, chicken wings, shaved ice. My friend got a mango drink with fresh mango in it! <br /><br />I\'m also surprised how many people come to Tracy Dessert after work. We came on a Sunday and the tables were always filled. I think the amount of tables they had were just perfect because no one really waited for seats for a long time, but the tables kept filling up once a table was finished.',
    'This place has gone down hill.  Clearly they have cut back on staff and food quality<br /><br />Many of the reviews were written before the menu changed.  I\'ve been going for years and the food quality has gone down hill.<br /><br />The service is slow & my salad, which was $15, was as bad as it gets.<br /><br />It\'s just not worth spending the money on this place when there are so many other options.',
    'I was really looking forward to visiting after having some of their beers. The \"Man O\'War\" quickly became my favorite DIPA; the Rusulka Vanilla Stout is a good thick, sweet stout; and the Ironclad is a top notch IPA. <br />The only big miss on their beers I\'ve had is the Big Chuck Barleywine. It could probably benefit greatly with age, but at this age all there is to taste is the alcohol.  <br />Nonetheless, I had enough to convince me that the other beers I hadn\'t had from them would be top notch... and they are! <br />The reason for the 2 stars should not reflect the quality of the brewers, they obviously know their craft well! <br />The servers are great and friendly.... but relying on two servers to wait on 100+ customers says a lot about how inexperienced management must be. In fact, after waiting 15 mins at a dirty table I was finally able to track down someone I guessed was an employee to let them know we were even there! <br />After another 5+ mins, the GM finally stopped over to take our drink order. The smugness of this guy was amazing. The thought of offering a simple apology never seemed to enter into his head. <br />This is the time a server finally stopped by to pick up the non-final check left by the party before us... who didn\'t seem very pleased when leaving. <br />The toast & cheese was good, but by the time we were able to dig into their heartiest offering of food, saltines and butter may have been equally pleasing.',
    'It\'s a giant Best Buy with 66 registers.  I don\'t get it.  What\'s the big deal about this place??',
]

### Routes
@app.route('/', methods=['GET'])
def home():
    """Renders the home page using the base index template."""
    selector = randint(0,9)
    return render_template(
        template_name_or_list = 'index.html',
        home='active',
        review=reviews[selector],
        stars=stars[selector]
    )

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', about='active')

@app.route('/bio', methods=['GET'])
def bio():
    return render_template('bio.html', bio='active')

@app.route('/predict', methods=['GET', 'POST'])
def predictor():
    if request.method == 'GET':
        return render_template('predict.html', predictor='active')
    user_review = request.form['user_review']
    user_review = [user_review]
    user_review = model.vectorizer.transform(user_review)
    prediction = stacked_prediction(model.models, model.ensemble, user_review)
    if prediction == 1:
        prediction = "Positive review: "
    elif prediction == 0:
        prediction = "Neutral review: "
    else:
        prediction = "Negative review: "
    linear_predict = model.linearSVR.predict(user_review)
    linear_predict = int(round(linear_predict[0]))
    if linear_predict < 1:
        linear_predict = 1
    elif linear_predict > 5:
        linear_predict = 5
    return render_template(template_name_or_list = 'predict.html',
                                predictor ='active',
                                prediction = prediction,
                                linear_predict = linear_predict
                                )