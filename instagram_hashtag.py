import instaloader

profile_list = ["alabamaallergyent","eyecentersouth","easternshorecosmeticsurgery","lyonscosmeticsurgerycenter","mclainsurgicalarts","totalskinandbeauty","neasecosmeticsurgery","drmelaniepetro","drbranman","englishplasticcosmeticsurgery","swetnamcosmeticsurgery","drsuzanneyee","drkathyduerksen","friedmanplastics","doctorheringer","bodybykotoske","esteticasurgery","thepoguecenterscottsdale","infinicosmetic","barbarinosurgicalarts","dr.thomasbarnes","boriscosmeticla","drgbrennan","cosmeticlaserdermatology","mfcdermatology","drchugay","drchugay","labellacosmeticsurgery","dr.julieedween","esthetica.ccs","cosmeticdoc","cosmeticlaserdermatology","plasticsurgerycentersdr90210","truecarecosmeticsurgery","drwhitneyflorin","dr.perfectself","cosmeticlaserdermatology","inlandcosmeticsurgery","adventknows","sacramentosurgicalarts","gregorykellermdfacs","eden_cosmetic_surgery","hkdermatology","esthetica.ccs","lombardocosmeticsurgery","aestheticlasercenter","lacosmeticdocs","harrymarshakmd","dr.m90210","dr.sidmirrafati","moeinsurgarts","aestheticarespa","sonobello","drmelaniepalm","powellcosmeticsurgery","sandiegosurgicalarts","foreveryoungcosmeticsurgery","drrobertrey","dermatologyinst","drkevinsadati","sdbodycontouring","michaelschwartzmd","esthetica.ccs","shumwaycosmetic","naturalimageoc","tabanmd","sonobello","inlandcosmeticsurgery","songoralsurgery","realdryou","modernsurgicalarts","drnesiba","alpineentco","thelangdoncenter","drstevenhoppingmd","lovethatbodydc","abuzenimd","dr.bedifined","ocosmeticsurgicalarts","305plastic_surgery","castellanocosmeticsurgery","facesbyfezza","azulcosmeticsurgery","ocosmeticsurgicalarts","drjiles_cosmetic_surgeon","dr.kass","mackmd","drjohnmartin","avanaplasticsurgery","xiluetplasticsurgery","drcosmeticsurg","carlossperamd","jolieplasticsurgery","drchipcole","meadowssurgicalarts","idealbodyinstitute","aestheticspecialtycentre","aestheticspecialtycentre","thefergusonclinic","drhiranaka","sturm.cosmetic.surgery","alpinesurgicalarts","summitdermatology","dr.cynthiabuono","drgeroulis","bodybybhanoo","chicagoplasticsurgery","hamiltonsurgicalarts","hamiltonsurgicalarts","hamiltonsurgicalarts","michiganentandallergy","sonobello","kansassurgicalarts","labellecosmeticsurgery","colemandermatology","drjkduplechain","williamsoncosmetic","drtreecesouthernaesthetics","realdrfeelgood","mddermatology","will_surgical_arts","michigancenter.cosmeticsurgery","drgeorgegoffas","birminghamcosmeticsurgery","dr.gregoryroche","michigancenter.cosmeticsurgery","omnicosmeticsurgery","baileycosmeticsurgery","sonobello","kcsurgicalarts","mcosmeticsurgery","nayakplasticsurgery","facialsurgerygroup","csipalmdesert","coleycosmetic","carolinascenterforcosmetics","carolinasurgicalarts","thecosmeticconcierge","facialsurgeryinstitute","omahabeautydoc","carniolplasticsurgery","doctor_corrado","thehughescenter","doclookgood","lasvegascosmeticsurgeon","roberttroell","alessimedspa","gordonandanmd","sdmedicalarts","newlook_newlife","hooman.khorasanimd","drkotlus","prasadcosmeticsurgery","sadickdermatology","drrobertschwarcz","dr_yoelshahar","drhowardsobel","drbfixin","drmattgoldschmidt","mandellbrownmd","drp_vip","visagesurgicalinstitute","yourbeauty_withdrnicole","tulsasurgicalarts","okccosmeticsurgeon","sonobello","cosmeticsurgeryaffiliates","cosmeticsurgeryspecialists","brandowclinic","skincentermd","providencefacialplastics","dr.allanwulc","imagesurgicalarts","marvelcosmetic_surgery","marvelcosmetic_surgery","marvelcosmetic_surgery","drdaisyayim","txsurgical","dr.daviddavila","bodevolvetx","northtexascosmeticsurgery","doctor_hah","alamooms","drjungmoney","warrenjkatzmd","drrussellkridel","drnewlifecosmetics","toceyeandface","noblecosmeticsurgeryplano","thepearldermatology","elite_cosmetic_surgery","rgvcosmetic","cosmeticsurgeryaffiliates","windsofchange_cosmeticsurgery","mansfieldcosmeticsurgery","yarishmd","constantinecosmeticsurgery","envision.surgery","vincentsurgical","rostamiopc","a2zenmd","adarasurgicalinstitute","tao_cosmeticsurgery","realdrj","shapecosmeticsurgery","labelleviecosmetic","dr.yirae.ort","realdrseattle","andersonsobelcosmetic","stiller_aesthetics","drtarbet","evivamd","belredcenter","allureskinhealth","akkary.surgery.center"]
profile_objects = []

#type in Instagram username
username = ""
#type in Instagram password
password = ""

n = 0
m = 0

#get instance
L = instaloader.Instaloader()

#login
L.login(username, password)

#get profiles
for p in profile_list:
    profile_objects.append(instaloader.Profile.from_username(L.context, p))
        
#count hashtag use
for profile in profile_objects:
    for i in profile.get_posts():
        if "plasticsurgeon" in i.caption_hashtags:
            n += 1
        if "plasticsurgery" in i.caption_hashtags:
            m += 1
    print(profile, n, m, sep = ",")
    n = 0
    m = 0
