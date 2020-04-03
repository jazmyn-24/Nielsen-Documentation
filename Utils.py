from pymongo import MongoClient
import Settings

def connect_mongo():
    #MONGO = Settings.MONGO_SERVER
    #PORT = Settings.MONGO_PORT
    # username = Settings.MONGO_USER
    # password = Settings.MONGO_PASS
    database = Settings.MONGO_DATABASE
    # connection = MongoClient('mongodb://cos-tccc-ebt-dev:agbi8w1dIVykarU9z8Kf0bwGEMnyS4LW9iWRA7gYsJoLjQpUGjQUNkZsWhehjQ1CSLoapF0xgXK5p8NUAlpN6g==@cos-tccc-ebt-dev.mongo.cosmos.azure.com:10255/EnrichmentDocs?ssl=true&replicaSet=globaldb&retrywrites=false')
    # connection = MongoClient(MONGO, PORT ,username=username ,password=password)
    connection = MongoClient('mongodb://cos-tccc-ebt-dev:agbi8w1dIVykarU9z8Kf0bwGEMnyS4LW9iWRA7gYsJoLjQpUGjQUNkZsWhehjQ1CSLoapF0xgXK5p8NUAlpN6g==@cos-tccc-ebt-dev.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cos-tccc-ebt-dev@', retrywrites=False)


    return connection[database]

exclusion_list=["amazon.com","youtube.com","wikipedia.org","facebook.com","ebay.com","indiamart.com","amazon.co.uk","pinterest.com","myfitnesspal.com","walmart.com","amazon.in","yummly.com","alibaba.com","thespruceeats.com","bevnet.com","allrecipes.com","influenster.com","fooducate.com","mysupermarket.co.uk","instacart.com","ebay.co.uk","woolworths.com.au","tradeindia.com","wordpress.com","wikihow.com","yahoo.com","heb.com","tesco.com","exportersindia.com","caffeineinformer.com","ocado.com","bigbasket.com","healthline.com","trndmonitor.com","fatsecret.com","ebay.com.au","livestrong.com","yelp.com","vitacost.com","quora.com","webmd.com","twitter.com","calorieking.com","ndtv.com","bodybuilding.com","luckyvitamin.com","absolutdrinks.com","issuu.com","waitrose.com","thirstydudes.com","samsclub.com","recipeofhealth.com","researchgate.net","hollandandbarrett.com","tarladalal.com","finewaters.com","verywellfit.com","morrisons.com","iherb.com","google.com","scielo.br","bevindustry.com","myshopping.com.au","supplementpolice.com","leaf.tv","vegrecipesofindia.com","nespresso.com","tripadvisor.com","bis.gov.in","twinings.co.uk","productreview.com.au","dcmsme.gov.in","mercadolivre.com.br","openfoodfacts.org","nutracheck.co.uk","wegmans.com","dailymail.co.uk","mexgrocer.com","starbucks.com","foursquare.com","foodnetwork.com","barnonedrinks.com","mercato.com","b2brazil.com","eatthismuch.com","lipton.com","bhg.com","linkedin.com","iceland.co.uk","republicoftea.com","drinkwhat.com","foodbev.com","sciencedirect.com","ratetea.com","sfgate.com","wholefoodsmarket.com","coffeeam.com","indianyellowpages.com","myrecipes.com","reddit.com","thekitchn.com","allprices.com.au","shopwell.com","draxe.com","realfoods.co.uk","teabox.com","thedailymeal.com","specialtyfood.com","monin.com","costco.com","geniuskitchen.com","indiatimes.com","steepster.com","1mg.com","thedrinkshop.com","buytea.com","organicfacts.net","seriouseats.com","nih.gov","fatsecret.com.au","dizzyfrinks.com","diligentchef.com","locu.com","flipkart.com","target.com","quill.com","scribd.com","illy.com","jet.com","lavazza.com","revolvy.com","swiggy.com","gnc.com","snapdeal.com","fandom.com","tasteofhome.com","amazon.it","myfooddiary.com","reviewstream.com","caffe.com","telegraph.co.uk","ebay.it","filstop.com","yummytummyaarthi.com","bbcgoodfood.com","marthastewart.com","dolphinfitness.co.uk","mercadolibre.com.mx","nytimes.com","instagram.com","healthambition.com","discountcoffee.com","mouthsofmums.com.au","hannaford.com","approvedfood.co.uk","adagio.com","welchs.com","sparkpeople.com","timesofindia.com","webstaurantstore.com","bluesoft.com.br","aquagrade.com","trendhunter.com","go4worldbusiness.com","supercall.com","etsy.com","zomato.com","mercola.com","ipfs.io","prweb.com","lifehack.org","roastandground.shop","supplementreviews.com","swansonvitamins.com","foodingredientsfirst.com","winc.com.au","nextdaycoffee.co.uk","panjiva.com","khanapakana.com","taste.com.au","drinksupermarket.com","englishteastore.com","buycott.com","harrisfarm.com.au","delishably.com","minimalistbaker.com","walmart.ca","apple.com","foodviva.com","offerscheck.co.uk","assamicaagro.in","eatthis.com","tastyquery.com","21food.com","curejoy.com","archive.org","littlecoffeeplace.com","aqua-calc.com","organicshop.in","stashtea.com","amazon.ca","epicurious.com","coffeebean.com","wholefoodsmagazine.com","dailymotion.com","steptohealth.com","talkingretail.com","specialtysodas.com","burpy.com","yummly.co.uk","msn.com","amigofoods.com","communitycoffee.com","whittard.co.uk","myfitnesspal.it","healthysupplies.co.uk","aussiehealthproducts.com.au","healthfully.com","taldepot.com","healthyfoods-online.com","vitaminshoppe.com","ozbargain.com.au","jayshreetea.com","shophealthy.in","coffeeorbust.com","wisegeek.com","coffeereview.com","fao.org","walgreens.com","thesodajerks.net","thewaterdeliverycompany.com","shopee.com.my","bestproducts.com","behance.net","smirnoff.com","enjoybettercoffee.com","picclick.com.au","coffeeforless.com","catawiki.com","prnewswire.com","rwknudsenfamily.com","wellnessmama.com","thrivemarket.com","sodapopstop.com","aqua-amore.com","vahdamteas.com","ishopindian.com","hy-vee.com","gunz.cc","planetorganic.com","sailusfood.com","thrillist.com","shoprite.com","made-in-china.com","delish.com","drinksmixer.com","teaforte.com","theteaspot.com","thegrocerygeek.com.au","weiku.com","oureverydaylife.com","foodstufffinds.co.uk","cafebritt.com","priceplow.com","foodzu.com","myshopify.com","shopclues.com","teareviewblog.com","dietspotlight.com","simplyorangejuice.com","reverso.net","totalwine.com","beveragedaily.com","shopee.ph","booking.com","fitbit.com","preparedfoods.com","placeoforigin.in","keurig.com","consumerreports.org","bestwaywholesale.co.uk","coca-colacompany.com","slideshare.net","organicgroceryusa.com","self.com","kroger.com","pinterest.pt","tropicana.com","costcobusinessdelivery.com","alegrofoods.com","okyalo.com","qualityfoods.com.au","tesco.pl","crecipe.com","nativealimentos.com.br","findglocal.com","goodhousekeeping.com","cappuccinosupreme.com","chowhound.com","ec21.com","gourmet-coffee.com","foodandwine.com","theyummylife.com","spoonuniversity.com","ceneo.pl","staples.com","snapple.com","a1supplements.com","nutritionexpress.com","whiskaffair.com","nectar.com","wikia.com","teatulia.com","ratebeer.com","bizrate.com","archanaskitchen.com","maxicoffee.com","iafstore.com","tesco.hu","juicyjuice.com","coca-colajourney.com.au","capsulehouse.coffee","polyphenolics.com","medicalnewstoday.com","thehindu.com","cafejurere.com.br","naturawater.com","naturalproductsexpo.com","fivestarsoda.com","naturalfoodseries.com","indianhealthyrecipes.com","liquor.com","ninfarea.com","oceanspray.com","beveragesdirect.com","asda.com","ewg.org","sunrichaqua.com","top10homeremedies.com","teadog.com","tea-and-coffee.com","juicegrape.com","independent.co.uk","efooddepot.com","globalhealingcenter.com","newhope.com","beverfood.com","breakdownweight.com","teasugar.in","hotfrog.com.au","halmaritea.com","thenibble.com","dolepineapplejuice.com","clipper-teas.com","acquapanna.com","groupon.com","tastebells.com","arborteas.com","coffeestrong.org","popsugar.com","shape.com","abelandcole.co.uk","danmurphys.com.au","pinterest.com.au","coca-cola.co.uk","cupandleaf.com","natureshealthbox.co.uk","medium.com","esupplements.com","realsimple.com","oldorchard.com","fever-tree.com","superama.com.mx","theguardian.com","diffordsguide.com","sororiteasisters.com","foodbabe.com","thefreedictionary.com","fatsecret.co.uk","detoxdietcleansev.com","wordreference.com","makemeacocktail.com","cw-usa.com","mineral-calculator.com","instructables.com","centralmarket.com","naturesflavors.com","coffeejudge.co.uk","inflibnet.ac.in","governmentgazette.sa.gov.au","choice.com.au","quizlet.com","hawaiicoffeecompany.com","wikivisually.com","bloomberg.com","godairyfree.org","espressocoffeeguide.com","readanddigest.com","thegrocer.co.uk","fitnessmagazine.com","fdin.org.uk","smh.com.au","academia.edu","lorespresso.com","tealyra.com","a1coffee.net","reference.com","spicesofindia.co.uk","wivelly.com","wabel.com","skipthepie.org","businesswire.com","teameteas.com","myprotein.com","blogspot.com","paytmmall.com","tumblr.com","loseweightbyeating.com","aapkipasandtea.com","inc42.com","hospitalitybizindia.com","bike24.com","company-list.org","target2000.net","businessinsider.com","cookingforengineers.com","eater.com","pennygolightly.com","wordpress.com","snapdeal.com","paytm.com","bestbuy.com"]