"""
PlantCare AI — reference information for all 38 classes in the
New Plant Diseases Dataset (vipoooool/new-plant-diseases-dataset).

Each entry supplies human-readable names, health status, and agronomic
guidance for academic / demo use. Always confirm diagnoses with a
qualified plant pathologist or extension service for real crop decisions.
"""

DISEASE_INFO = {
    "Apple___Apple_scab": {
        "plant_name": "Apple",
        "disease_name": "Apple scab",
        "is_healthy": False,
        "description": (
            "Apple scab is a fungal disease caused by Venturia inaequalis that "
            "produces olive-green to dark brown velvety spots on leaves and fruit. "
            "Severe infections can cause premature leaf drop and misshapen, cracked fruit."
        ),
        "solution": (
            "1. Remove and destroy fallen infected leaves and fruit to reduce spore sources.\n"
            "2. Apply protectant fungicides (e.g., captan) at green tip, pink, petal fall, and cover sprays per local extension schedules.\n"
            "3. For organic orchards, use sulfur or lime sulfur where labeled, following temperature restrictions.\n"
            "4. Improve air circulation through proper pruning and avoiding overhead irrigation.\n"
            "5. Reapply fungicides after heavy rain according to product label intervals."
        ),
        "prevention": (
            "• Plant scab-resistant cultivars where available.\n"
            "• Rake and compost or discard fallen leaves in autumn.\n"
            "• Space trees for sunlight and airflow; avoid wetting foliage when irrigating.\n"
            "• Monitor weather during wet springs and begin sprays before infection periods."
        ),
    },
    "Apple___Black_rot": {
        "plant_name": "Apple",
        "disease_name": "Black rot (frogeye leaf spot / fruit rot)",
        "is_healthy": False,
        "description": (
            "Black rot is caused by the fungus Botryosphaeria obtusa and appears as "
            "purple leaf spots that expand with concentric rings, cankers on branches, "
            "and firm brown rot on fruit. Warm, humid weather favors spread."
        ),
        "solution": (
            "1. Prune out dead wood, cankers, and mummified fruit; disinfect tools between cuts.\n"
            "2. Remove nearby alternate hosts such as infected juniper where relevant to the pathogen complex.\n"
            "3. Apply fungicides timed for blossom and summer cover sprays; follow regional IPM guidelines.\n"
            "4. Improve tree vigor with balanced fertility and irrigation; avoid bark wounds.\n"
            "5. Harvest fruit carefully and store only sound apples to limit storage rots."
        ),
        "prevention": (
            "• Maintain sanitation in the orchard year-round.\n"
            "• Avoid injuries from mowers, string trimmers, and ladders.\n"
            "• Use resistant rootstocks and cultivars when practical.\n"
            "• Scout early for leaf spots and branch cankers and act promptly."
        ),
    },
    "Apple___Cedar_apple_rust": {
        "plant_name": "Apple",
        "disease_name": "Cedar-apple rust",
        "is_healthy": False,
        "description": (
            "This rust disease requires both apple and juniper (cedar) hosts to complete its life cycle. "
            "Bright orange-yellow spots on apple leaves and fruit are common in spring after infection."
        ),
        "solution": (
            "1. Remove nearby alternate-host junipers within several hundred yards if feasible.\n"
            "2. Apply fungicides from pink through first cover sprays; continue on a label-based interval in wet years.\n"
            "3. Plant rust-resistant apple varieties for long-term reduction in spray need.\n"
            "4. Improve airflow to speed leaf drying after rain or dew.\n"
            "5. Record infection timing each year to refine next season’s spray calendar."
        ),
        "prevention": (
            "• Choose resistant cultivars for new plantings.\n"
            "• Avoid planting apples downwind of heavy juniper plantings.\n"
            "• Time irrigation to keep foliage dry when possible.\n"
            "• Combine cultural tactics with timely fungicides in high-risk sites."
        ),
    },
    "Apple___healthy": {
        "plant_name": "Apple",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "The foliage and fruit appear consistent with a healthy apple tree without "
            "obvious signs of the common apple diseases in this dataset. Continue routine "
            "orchard monitoring because health status can change with weather and pest pressure."
        ),
        "solution": (
            "1. No disease treatment is required based on this prediction.\n"
            "2. Continue standard integrated pest management: scouting, nutrition, and water management.\n"
            "3. Keep records of bloom dates, sprays, and weather for next season’s planning.\n"
            "4. Re-check suspicious areas if symptoms develop later in the season."
        ),
        "prevention": (
            "• Maintain balanced fertilization and soil pH suited to apples.\n"
            "• Prune annually for structure, light penetration, and air movement.\n"
            "• Monitor for insects and diseases weekly during the growing season.\n"
            "• Mulch and manage weeds to reduce competition and bark damage."
        ),
    },
    "Blueberry___healthy": {
        "plant_name": "Blueberry",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "Leaves and shoots resemble healthy highbush or rabbiteye blueberry plants "
            "without the common foliar disease signatures represented in this dataset. "
            "Ongoing care should still include soil acidity and irrigation management."
        ),
        "solution": (
            "1. No disease-specific treatment is indicated by this image alone.\n"
            "2. Continue acidifying irrigation/fertilization if soil tests show high pH.\n"
            "3. Maintain consistent moisture, especially during fruit sizing.\n"
            "4. Scout for mummy berry, anthracnose, or gall if new symptoms appear."
        ),
        "prevention": (
            "• Keep soil pH roughly 4.5–5.5 depending on species and local recommendations.\n"
            "• Use pine mulch and avoid excessive nitrogen that promotes succulent growth.\n"
            "• Prune annually to renew wood and improve light inside the canopy.\n"
            "• Remove wild blueberry relatives nearby that may harbor pests."
        ),
    },
    "Cherry___Powdery_mildew": {
        "plant_name": "Cherry",
        "disease_name": "Powdery mildew",
        "is_healthy": False,
        "description": (
            "Powdery mildew on cherry is caused by Podosphaera clandestina and shows as "
            "white powdery patches on leaves and distorted shoots. Infected fruit may russet "
            "or crack, reducing market quality."
        ),
        "solution": (
            "1. Apply labeled fungicides beginning pre-bloom through shuck fall on susceptible varieties.\n"
            "2. Use sulfur or other materials approved for cherries per local restrictions.\n"
            "3. Improve canopy airflow with selective pruning.\n"
            "4. Avoid excessive nitrogen that produces lush, susceptible growth.\n"
            "5. Rotate fungicide modes of action to delay resistance development."
        ),
        "prevention": (
            "• Plant less susceptible cultivars where powdery mildew is chronic.\n"
            "• Avoid overcrowding; train trees to open vase or central leader forms.\n"
            "• Irrigate at soil level when possible to limit prolonged leaf wetness.\n"
            "• Remove severely infected shoots during dormant pruning."
        ),
    },
    "Cherry___healthy": {
        "plant_name": "Cherry",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "The cherry foliage appears generally free of the disease patterns in this "
            "dataset. Sweet and tart cherries still benefit from routine monitoring for "
            "bacterial canker, leaf spot, and insect damage."
        ),
        "solution": (
            "1. No disease treatment is required from this prediction alone.\n"
            "2. Continue dormant sanitation and summer scouting.\n"
            "3. Maintain irrigation and nutrition to avoid drought or deficiency stress.\n"
            "4. Document any new spots or oozing bark for timely expert review."
        ),
        "prevention": (
            "• Avoid pruning in wet weather to reduce bacterial canker risk.\n"
            "• Use clean tools; disinfect between trees when pathogens are suspected.\n"
            "• Mulch to moderate soil temperature and moisture swings.\n"
            "• Follow regional spray guides only when pests or diseases exceed thresholds."
        ),
    },
    "Corn___Cercospora_leaf_spot": {
        "plant_name": "Corn",
        "disease_name": "Gray leaf spot (Cercospora leaf spot)",
        "is_healthy": False,
        "description": (
            "Gray leaf spot, caused by Cercospora zeae-maydis, produces rectangular tan to "
            "gray lesions bounded by leaf veins. Yield loss increases when lesions reach the "
            "ear leaf before silking under prolonged humid conditions."
        ),
        "solution": (
            "1. Rotate away from corn for at least one year; manage crop residue that harbors inoculum.\n"
            "2. Choose hybrids with strong gray leaf spot ratings for your region.\n"
            "3. Apply foliar fungicides at tasseling if disease is progressing toward the ear zone and weather favors spread.\n"
            "4. Improve drainage and avoid excessive plant density in irrigated fields.\n"
            "5. Combine tactics with scouting maps to target worst fields first."
        ),
        "prevention": (
            "• Till or incorporate residue only where erosion risk allows and labels permit.\n"
            "• Avoid continuous corn where gray leaf spot is established.\n"
            "• Balance nitrogen to healthy canopy growth without excessive rankness.\n"
            "• Scout lower leaves from mid-season onward in humid regions."
        ),
    },
    "Corn___Common_rust": {
        "plant_name": "Corn",
        "disease_name": "Common rust",
        "is_healthy": False,
        "description": (
            "Common rust (Puccinia sorghi) forms small cinnamon-brown pustules on upper "
            "and lower leaf surfaces. It is usually favored by cool, humid weather and can "
            "reduce photosynthesis if lesions become numerous before grain fill."
        ),
        "solution": (
            "1. Select hybrids with good rust resistance/tolerance.\n"
            "2. Apply fungicide if rust reaches the ear leaf early and favorable weather continues.\n"
            "3. Ensure adequate potassium based on soil tests to support plant health.\n"
            "4. Avoid unnecessary late nitrogen that delays maturity in high-risk fields.\n"
            "5. Track regional rust reports to anticipate epidemic years."
        ),
        "prevention": (
            "• Use crop rotation and residue management as part of an IPM plan.\n"
            "• Plant at recommended populations for soil productivity.\n"
            "• Monitor fields weekly from late vegetative stages through dent.\n"
            "• Keep records of hybrid performance to refine future selections."
        ),
    },
    "Corn___Northern_Leaf_Blight": {
        "plant_name": "Corn",
        "disease_name": "Northern corn leaf blight",
        "is_healthy": False,
        "description": (
            "Northern corn leaf blight (Exserohilum turcicum) causes long elliptical gray-green "
            "to tan lesions. Severe epidemics under warm, wet conditions can substantially reduce yields."
        ),
        "solution": (
            "1. Rotate crops and bury or manage infected residue where practical.\n"
            "2. Plant resistant hybrids matched to local pathogen races when available.\n"
            "3. Apply tassel-stage fungicides if lesions are moving up the canopy and weather remains wet.\n"
            "4. Address fertility and drainage issues that stress plants.\n"
            "5. Combine aerial or ground application with accurate gallon rates for coverage."
        ),
        "prevention": (
            "• Avoid back-to-back corn on the same ground in high-pressure areas.\n"
            "• Scout the lower canopy early; NCLB often starts low and moves up.\n"
            "• Maintain balanced fertility; test soils every few years.\n"
            "• Use certified seed and handle equipment cleanly between fields."
        ),
    },
    "Corn___healthy": {
        "plant_name": "Corn",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "The corn leaf in the image resembles healthy tissue without strong signatures "
            "of the foliar diseases in this benchmark set. Field-level decisions should still "
            "consider growth stage, hybrid, and recent weather."
        ),
        "solution": (
            "1. No foliar disease treatment is indicated by this image alone.\n"
            "2. Continue scouting for rust, blights, and stalk rots through maturity.\n"
            "3. Manage irrigation and nitrogen to support steady development.\n"
            "4. Flag any odd lesions for closer inspection or lab testing if they spread."
        ),
        "prevention": (
            "• Follow hybrid placement guides for your soils and disease history.\n"
            "• Control weeds that may host pathogens or compete for moisture.\n"
            "• Harvest on time to reduce stalk lodging and ear molds.\n"
            "• Preserve soil structure with reduced tillage where appropriate."
        ),
    },
    "Grape___Black_rot": {
        "plant_name": "Grape",
        "disease_name": "Black rot",
        "is_healthy": False,
        "description": (
            "Black rot of grape is caused by Guignardia bidwellii and produces tan leaf spots "
            "with black pycnidia and hard, shriveled ‘mummies’ on clusters. Warm, rainy springs "
            "drive severe fruit loss in susceptible cultivars."
        ),
        "solution": (
            "1. Remove mummified berries and prune out infected canes during dormancy.\n"
            "2. Open the canopy for sunlight and air; leaf removal around clusters can help where permitted.\n"
            "3. Apply protectant and systemic fungicides on a tight schedule from immediate pre-bloom through 4–6 weeks post-bloom.\n"
            "4. Eliminate wild grapes near the vineyard that can harbor inoculum.\n"
            "5. Re-treat after rains exceeding label thresholds."
        ),
        "prevention": (
            "• Site vineyards on slopes with good air drainage.\n"
            "• Choose cultivars with lower black rot susceptibility for humid regions.\n"
            "• Maintain ground cover that reduces soil splash onto fruit zones.\n"
            "• Keep detailed spray records and adjust programs after wet years."
        ),
    },
    "Grape___Esca": {
        "plant_name": "Grape",
        "disease_name": "Esca (black measles / grapevine trunk disease)",
        "is_healthy": False,
        "description": (
            "Esca is a complex of fungal pathogens affecting grapevine wood and foliage. "
            "Interveinal necrosis, tiger-stripe patterns, and berry spotting may appear in "
            "summer, often following stress or pruning wounds."
        ),
        "solution": (
            "1. Remove severely affected vines; replace with certified nursery stock.\n"
            "2. Avoid large pruning wounds during rainy periods; paint large cuts if recommended locally.\n"
            "3. Improve vine balance through canopy and crop load management.\n"
            "4. There is no single curative spray; focus on sanitation and vine vigor.\n"
            "5. Consult viticulture specialists for trunk surgery options on valuable vines."
        ),
        "prevention": (
            "• Use clean pruning tools; disinfect between vines in diseased blocks.\n"
            "• Delay major pruning until late winter when wounds heal faster.\n"
            "• Avoid repeated mechanical bark injury from ties or equipment.\n"
            "• Monitor young vineyards closely; early removal slows inoculum buildup."
        ),
    },
    "Grape___Leaf_blight": {
        "plant_name": "Grape",
        "disease_name": "Leaf blight (Isariopsis leaf spot)",
        "is_healthy": False,
        "description": (
            "This pattern is commonly associated with Isariopsis clavispora and related leaf "
            "spotting in humid grape regions. Lesions expand and can defoliate weak vines if "
            "left unmanaged during wet seasons."
        ),
        "solution": (
            "1. Apply labeled fungicides used for other foliar diseases where leaf blight is confirmed.\n"
            "2. Improve canopy airflow through shoot positioning and basal leaf removal where appropriate.\n"
            "3. Reduce cluster zone humidity with open training systems.\n"
            "4. Remove heavily infected leaves on young vines to protect permanent wood.\n"
            "5. Coordinate sprays with downy and powdery mildew programs to minimize passes."
        ),
        "prevention": (
            "• Avoid excessive shoot density and shading inside the canopy.\n"
            "• Manage irrigation to limit long wetting events on leaves.\n"
            "• Scout after storms; many blights explode following wind-driven rain.\n"
            "• Keep weeds controlled to improve air movement at the cordon."
        ),
    },
    "Grape___healthy": {
        "plant_name": "Grape",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "The grape leaf appears generally healthy relative to the disease classes in this "
            "dataset. Vineyard managers should still track mildew, botrytis, and rot based on "
            "bloom stage and weather models."
        ),
        "solution": (
            "1. No disease intervention is strictly required from this image alone.\n"
            "2. Continue preventive programs aligned with local extension calendars.\n"
            "3. Monitor cluster zones as berries soften; rot risk rises near harvest.\n"
            "4. Adjust leaf removal and cluster thinning to balance sun exposure and disease risk."
        ),
        "prevention": (
            "• Maintain balanced vines: neither weak nor overly vigorous.\n"
            "• Calibrate sprayers annually for coverage on both leaf surfaces.\n"
            "• Record rainfall and spray intervals to defend high-pressure periods.\n"
            "• Train crews to spot early mildew oil spots and oil spots on fruit."
        ),
    },
    "Orange___Haunglongbing": {
        "plant_name": "Orange (citrus)",
        "disease_name": "Huanglongbing (HLB; citrus greening)",
        "is_healthy": False,
        "description": (
            "HLB is a devastating bacterial disease spread primarily by Asian citrus psyllid. "
            "Blotchy mottling, asymmetric chlorosis, and twig dieback are common foliar signs, "
            "while fruit may be small, lopsided, and off-flavor."
        ),
        "solution": (
            "1. Report suspected HLB to agricultural officials where mandatory scouting exists.\n"
            "2. Intensively manage psyllid populations with labeled insecticides and biological controls per regional IPM.\n"
            "3. Optimize nutrition and irrigation to maintain tree productivity while research continues.\n"
            "4. Remove confirmed positive trees where regulations require to slow spread.\n"
            "5. Follow university extension guides for trunk injection trials only under legal permits."
        ),
        "prevention": (
            "• Use certified budwood and screen houses for new plantings in endemic areas.\n"
            "• Scout frequently for psyllid adults and nymphs, especially on new flush.\n"
            "• Coordinate area-wide treatments with neighbors when feasible.\n"
            "• Remove abandoned citrus that serves as a reservoir."
        ),
    },
    "Peach___Bacterial_spot": {
        "plant_name": "Peach",
        "disease_name": "Bacterial spot",
        "is_healthy": False,
        "description": (
            "Bacterial spot (Xanthomonas arboricola pv. pruni) causes angular water-soaked "
            "leaf spots, shot holes, and fruit cracking. Warm, windy, rainy weather promotes "
            "epidemics, especially on susceptible cultivars."
        ),
        "solution": (
            "1. Plant resistant cultivars and rootstocks where bacterial spot is chronic.\n"
            "2. Apply copper and/or oxytetracycline programs strictly per label and local timing windows.\n"
            "3. Avoid overhead irrigation and mechanical injury during wet periods.\n"
            "4. Improve airflow with pruning; avoid excessive nitrogen.\n"
            "5. Remove severely affected limbs to reduce inoculum in young orchards."
        ),
        "prevention": (
            "• Site orchards with good air drainage away from low frost pockets that prolong leaf wetness.\n"
            "• Delay pruning to dry weather; disinfect tools between trees.\n"
            "• Scout shucks and young leaves early; first lesions guide spray initiation.\n"
            "• Keep weed strips mowed to hasten drying of lower canopy."
        ),
    },
    "Peach___healthy": {
        "plant_name": "Peach",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "Peach foliage appears broadly healthy in the sense of this dataset’s classes. "
            "Stone fruits still require attention to brown rot, peach leaf curl (where present), "
            "and insect pests through the season."
        ),
        "solution": (
            "1. No bacterial or fungal spot treatment is indicated by this image alone.\n"
            "2. Continue dormant copper or lime sulfur where peach leaf curl is a risk (regions vary).\n"
            "3. Thin fruit and manage water to size quality crops.\n"
            "4. Scout for oriental fruit moth and other pests at appropriate degree-days."
        ),
        "prevention": (
            "• Maintain open vase or perpendicular V training for light and spray penetration.\n"
            "• Avoid bark damage from equipment and rodents.\n"
            "• Mulch to conserve moisture without burying trunk flare.\n"
            "• Soil test periodically; correct potassium and boron deficiencies as advised."
        ),
    },
    "Pepper___Bacterial_spot": {
        "plant_name": "Pepper",
        "disease_name": "Bacterial spot",
        "is_healthy": False,
        "description": (
            "Bacterial spot on pepper (Xanthomonas spp.) creates small greasy leaf spots with "
            "yellow halos and raised corky lesions on fruit. Splashing rain and contaminated "
            "seed or transplants spread the bacteria rapidly."
        ),
        "solution": (
            "1. Apply labeled copper/maneb programs beginning before symptoms appear in high-risk fields.\n"
            "2. Switch to drip irrigation; avoid working wet plants.\n"
            "3. Remove heavily infected lower leaves if sanitary and allowed.\n"
            "4. Rotate away from solanaceous crops for 2–3 years where feasible.\n"
            "5. Use certified transplants; rogue infected seedlings early."
        ),
        "prevention": (
            "• Treat seed with hot water or buy certified pathogen-free seed.\n"
            "• Sanitize stakes, tools, and greenhouse benches.\n"
            "• Avoid overhead watering in humid climates.\n"
            "• Choose tolerant varieties when available for your market."
        ),
    },
    "Pepper___healthy": {
        "plant_name": "Pepper",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "Pepper leaves look generally healthy compared with the bacterial spot class in "
            "this dataset. Continue monitoring for aphids, mites, and fungal issues during "
            "fruit set and ripening."
        ),
        "solution": (
            "1. No disease-specific treatment is required from this prediction alone.\n"
            "2. Maintain steady moisture; avoid boom-bust irrigation cycles.\n"
            "3. Fertilize according to soil tests and growth stage.\n"
            "4. Scout undersides of leaves weekly for early pest detection."
        ),
        "prevention": (
            "• Use mulch to reduce soil splash onto foliage.\n"
            "• Space plants for airflow in high tunnels and open fields.\n"
            "• Rotate crops and manage solanaceous volunteers.\n"
            "• Sanitize hands and tools when moving between diseased and healthy blocks."
        ),
    },
    "Potato___Early_blight": {
        "plant_name": "Potato",
        "disease_name": "Early blight",
        "is_healthy": False,
        "description": (
            "Early blight (Alternaria solani) forms dark concentric-ring lesions, often first on "
            "older leaves. It is favored by warm temperatures and plant stress, and can reduce "
            "tubers when defoliation occurs before bulking finishes."
        ),
        "solution": (
            "1. Begin protectant fungicides when lesions first appear on lower leaves; continue on label intervals.\n"
            "2. Improve fertility and irrigation to reduce plant stress.\n"
            "3. Ensure adequate nitrogen and potassium per soil tests.\n"
            "4. Top-kill vines on schedule to promote skin set before harvest.\n"
            "5. Store only dry, wound-free tubers at proper temperature and humidity."
        ),
        "prevention": (
            "• Rotate away from potatoes and tomatoes for multiple years in problem fields.\n"
            "• Plant certified seed tubers.\n"
            "• Avoid excessive irrigation frequency that keeps leaves wet.\n"
            "• Destroy cull piles that harbor Alternaria inoculum."
        ),
    },
    "Potato___Late_blight": {
        "plant_name": "Potato",
        "disease_name": "Late blight",
        "is_healthy": False,
        "description": (
            "Late blight (Phytophthora infestans) causes water-soaked lesions that expand rapidly "
            "under cool, wet conditions, with white sporulation on leaf undersides in humid "
            "mornings. It can destroy canopies and rot tubers in storage."
        ),
        "solution": (
            "1. Apply fungicides preventively during high-risk weather; mix modes of action per resistance-management guides.\n"
            "2. Destroy volunteer potatoes and tomato debris.\n"
            "3. Hilling and vine killing should protect tubers from sporangia wash-down.\n"
            "4. Harvest when skins are set; avoid bruising.\n"
            "5. Ventilate storages; remove rotting tubers promptly."
        ),
        "prevention": (
            "• Plant resistant varieties where markets accept them.\n"
            "• Monitor regional late blight alerts and local spore trapping if available.\n"
            "• Use certified seed and reject lots with suspect symptoms.\n"
            "• Improve field drainage and row orientation for faster drying."
        ),
    },
    "Potato___healthy": {
        "plant_name": "Potato",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "Potato foliage appears broadly healthy relative to early and late blight patterns "
            "in this dataset. Hilling, irrigation, and nutrient programs should still follow "
            "best management practices for your region."
        ),
        "solution": (
            "1. No blight-specific treatment is indicated by this image alone.\n"
            "2. Continue scouting, especially during cool, wet spells.\n"
            "3. Manage Colorado potato beetle and aphids (virus vectors) per thresholds.\n"
            "4. Plan vine kill and harvest timing for tuber maturity and skin set."
        ),
        "prevention": (
            "• Use certified seed and handle seed pieces with clean equipment.\n"
            "• Rotate crops; control nightshade weeds.\n"
            "• Calibrate planters and sprayers for uniform emergence and coverage.\n"
            "• Record irrigation and weather to anticipate disease windows."
        ),
    },
    "Raspberry___healthy": {
        "plant_name": "Raspberry",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "Raspberry leaves resemble healthy primocanes or floricanes without strong signs "
            "of the modeled diseases. Brambles still need management for anthracnose, spur blight, "
            "and viruses over time."
        ),
        "solution": (
            "1. No disease treatment is required from this prediction alone.\n"
            "2. Keep planting rows narrow; remove old floricanes after harvest.\n"
            "3. Maintain trellis wires to improve airflow.\n"
            "4. Scout for cane borers and leaf spot if weather turns wet."
        ),
        "prevention": (
            "• Plant virus-indexed stock from reputable nurseries.\n"
            "• Avoid planting near wild brambles.\n"
            "• Mulch for moisture consistency and weed suppression.\n"
            "• Irrigate with drip to keep canopies drier."
        ),
    },
    "Soybean___healthy": {
        "plant_name": "Soybean",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "Soybean leaflets appear generally healthy in the context of this dataset. Season-long "
            "scouting remains important for frogeye leaf spot, cercospora, and sudden death syndrome "
            "in susceptible rotations."
        ),
        "solution": (
            "1. No foliar disease treatment is indicated by this image alone.\n"
            "2. Continue integrated management for insects and diseases at economic thresholds.\n"
            "3. Monitor nodulation and tissue tests if yellowing unrelated to disease appears.\n"
            "4. Adjust variety maturity for your zone to reduce end-of-season stress."
        ),
        "prevention": (
            "• Rotate crops; manage drainage in SDS-prone fields.\n"
            "• Select varieties with strong disease packages for your geography.\n"
            "• Plant at recommended populations and planting dates.\n"
            "• Handle seed with care; use fungicide seed treatments as standard practice."
        ),
    },
    "Squash___Powdery_mildew": {
        "plant_name": "Squash",
        "disease_name": "Powdery mildew",
        "is_healthy": False,
        "description": (
            "Powdery mildew on cucurbits (Podosphaera xanthii and Erysiphe cichoracearum) forms "
            "white talcum-like colonies on leaves and stems. Severe infections reduce fruit size "
            "and quality, especially in dense plantings."
        ),
        "solution": (
            "1. Apply labeled fungicides or biofungicides at first detection; repeat per label.\n"
            "2. Use resistant cultivars for summer and winter squash where available.\n"
            "3. Open the canopy through proper spacing and trellising for vining types.\n"
            "4. Remove heavily infected old leaves on small plantings to improve spray coverage.\n"
            "5. Alternate FRAC groups to manage resistance in pathogen populations."
        ),
        "prevention": (
            "• Avoid excess nitrogen that produces lush, susceptible growth.\n"
            "• Irrigate at soil level; water early so leaves dry by evening.\n"
            "• Sanitize high tunnels between crops.\n"
            "• Scout weekly after vine run; mildew often begins on oldest leaves."
        ),
    },
    "Strawberry___Leaf_scorch": {
        "plant_name": "Strawberry",
        "disease_name": "Leaf scorch",
        "is_healthy": False,
        "description": (
            "Leaf scorch (Diplocarpon earlianum) causes purple to dark brown spots without "
            "distinctive white centers. Lesions can coalesce, giving a burned appearance and "
            "weakening plants over a season."
        ),
        "solution": (
            "1. Apply labeled fungicides on a protectant schedule during bloom and fruit development in wet years.\n"
            "2. Renovate matted-row plantings after harvest: narrow rows, fertilize, irrigate.\n"
            "3. Remove infected old leaves where practical in annual plasticulture systems.\n"
            "4. Improve drainage and use drip irrigation to limit leaf wetness.\n"
            "5. Start clean: use certified plants and avoid introducing diseased runners."
        ),
        "prevention": (
            "• Choose resistant cultivars where leaf spot complex is severe.\n"
            "• Mulch fruit to reduce splash and fruit rots.\n"
            "• Space plants for airflow; avoid overcrowded beds.\n"
            "• Scout after rains; early spots are easier to manage."
        ),
    },
    "Strawberry___healthy": {
        "plant_name": "Strawberry",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "Strawberry foliage appears generally healthy compared with leaf scorch in this "
            "dataset. Continue programs for gray mold, mites, and nutrition especially during "
            "flowering and fruiting."
        ),
        "solution": (
            "1. No disease-specific treatment is required from this prediction alone.\n"
            "2. Maintain mulch depth and drip schedules for steady growth.\n"
            "3. Remove diseased berries and leaves during harvest walks.\n"
            "4. Sample tissue or soil if unusual yellowing or stunting appears."
        ),
        "prevention": (
            "• Plant certified disease-free transplants.\n"
            "• Rotate new beds away from old infested sites when possible.\n"
            "• Control weeds that block airflow.\n"
            "• Sanitize tools when dividing plants."
        ),
    },
    "Tomato___Bacterial_spot": {
        "plant_name": "Tomato",
        "disease_name": "Bacterial spot",
        "is_healthy": False,
        "description": (
            "Bacterial spot on tomato (Xanthomonas spp.) produces small dark lesions with yellow "
            "halos and may cause defoliation and fruit speckling. Spread is rapid with splashing "
            "water, handling, and contaminated seed or transplants."
        ),
        "solution": (
            "1. Apply copper-based programs beginning at transplant or first sign; add mancozeb where labeled.\n"
            "2. Avoid overhead irrigation; work plants when dry.\n"
            "3. Rogue infected seedlings before setting.\n"
            "4. Rotate fields away from tomato and pepper for 2–3 years.\n"
            "5. Remove lower infected leaves carefully if it improves airflow without spreading bacteria."
        ),
        "prevention": (
            "• Use certified transplants from reputable greenhouses.\n"
            "• Hot-water treat seed only with exact university protocols.\n"
            "• Stake and prune to improve drying; sanitize pruners frequently.\n"
            "• Mulch soil to reduce splash onto foliage."
        ),
    },
    "Tomato___Early_blight": {
        "plant_name": "Tomato",
        "disease_name": "Early blight",
        "is_healthy": False,
        "description": (
            "Early blight (Alternaria solani) causes target-like lesions on older leaves and "
            "stem darkening near the soil line. Warm, humid periods and stressed plants favor "
            "rapid defoliation that reduces yield and sun-scalds fruit."
        ),
        "solution": (
            "1. Apply protectant fungicides beginning at first fruit set or when lesions appear low in the canopy.\n"
            "2. Stake plants; remove badly infected leaves to slow upward movement if sanitary.\n"
            "3. Mulch and use drip irrigation to reduce soil splash.\n"
            "4. Fertilize and water consistently to limit plant stress.\n"
            "5. At season end, remove or incorporate residue thoughtfully based on rotation plans."
        ),
        "prevention": (
            "• Rotate tomatoes with non-host crops.\n"
            "• Space plants for airflow; avoid excessive nitrogen.\n"
            "• Choose varieties with some tolerance where available.\n"
            "• Scout weekly from mid-season onward in humid climates."
        ),
    },
    "Tomato___Late_blight": {
        "plant_name": "Tomato",
        "disease_name": "Late blight",
        "is_healthy": False,
        "description": (
            "Late blight (Phytophthora infestans) on tomato causes greasy, irregular lesions and "
            "fuzzy sporulation on leaf undersides under moist conditions. It can kill plants "
            "within days and ruin green and ripe fruit."
        ),
        "solution": (
            "1. Apply fungicides preventively during alert periods; use products effective on oomycetes and rotate modes of action.\n"
            "2. Remove infected plants in home gardens; bag and discard—do not compost.\n"
            "3. Improve airflow in tunnels; ventilate overnight to dry foliage.\n"
            "4. Avoid overhead watering; irrigate at soil level.\n"
            "5. Destroy culls and volunteer tomatoes promptly."
        ),
        "prevention": (
            "• Buy locally adapted, tested transplants; inspect for odd lesions.\n"
            "• Monitor regional late blight maps and university alerts.\n"
            "• Plant resistant varieties where fruit type meets market needs.\n"
            "• Sanitize stakes and trellis materials between seasons."
        ),
    },
    "Tomato___Leaf_Mold": {
        "plant_name": "Tomato",
        "disease_name": "Leaf mold",
        "is_healthy": False,
        "description": (
            "Leaf mold (Passalora fulva) is common in greenhouses and high tunnels, causing "
            "yellow patches on upper leaf surfaces with olive-green mold below. High humidity "
            "with moderate temperatures drives epidemics."
        ),
        "solution": (
            "1. Ventilate and heat judiciously to keep relative humidity lower on leaves overnight.\n"
            "2. Apply labeled fungicides at first detection; improve spray coverage on leaf undersides.\n"
            "3. Remove infected lower leaves to improve airflow (when plants are dry).\n"
            "4. Avoid leaf wetting from misting or poorly timed irrigation.\n"
            "5. Consider resistant varieties for protected culture."
        ),
        "prevention": (
            "• Plant at adequate spacing; prune for an open canopy.\n"
            "• Use drip irrigation; mulch floors or use clean ground cover.\n"
            "• Disinfect structures between crops where economically feasible.\n"
            "• Scout early; leaf mold moves fast in stagnant humid air."
        ),
    },
    "Tomato___Septoria_leaf_spot": {
        "plant_name": "Tomato",
        "disease_name": "Septoria leaf spot",
        "is_healthy": False,
        "description": (
            "Septoria lycopersici produces small circular spots with dark borders and tan centers "
            "bearing tiny black pycnidia. It begins on oldest leaves and progresses upward, "
            "often after prolonged leaf wetness."
        ),
        "solution": (
            "1. Apply protectant fungicides after lower leaves first show spots; continue on intervals.\n"
            "2. Mulch to limit soil splash; stake and prune for airflow.\n"
            "3. Avoid overhead irrigation; water at the base early in the day.\n"
            "4. Remove severely infected leaves if it improves coverage and does not overly expose fruit to sunburn.\n"
            "5. Deep-turn or manage crop residue as part of a multi-year rotation plan."
        ),
        "prevention": (
            "• Rotate away from tomatoes and potatoes.\n"
            "• Destroy volunteer tomatoes.\n"
            "• Use drip and wide row spacing in humid regions.\n"
            "• Sanitize stakes and cages where disease was severe last season."
        ),
    },
    "Tomato___Spider_mites": {
        "plant_name": "Tomato",
        "disease_name": "Spider mite damage (two-spotted spider mite)",
        "is_healthy": False,
        "description": (
            "Spider mites are tiny arachnids that pierce cells, causing stippling, bronzing, and "
            "fine webbing on leaves. Hot, dry, dusty conditions favor explosive populations, "
            "especially along field edges and in protected culture."
        ),
        "solution": (
            "1. Confirm mites with a hand lens; treat thresholds per crop stage and market.\n"
            "2. Release or conserve predatory mites and minute pirate bugs where feasible.\n"
            "3. Apply labeled miticides, rotating modes of action; add adjuvants only as directed.\n"
            "4. Increase humidity slightly or rinse plants carefully in small-scale/high-value settings if practical.\n"
            "5. Remove heavily infested leaves on lower canopy to slow spread."
        ),
        "prevention": (
            "• Avoid broad-spectrum insecticides that flare mites by killing predators.\n"
            "• Control roadside dust; use windbreaks or sprinkler irrigation briefly during heat waves if appropriate.\n"
            "• Scout weekly on leaf undersides, especially downwind edges.\n"
            "• Quarantine new greenhouse plantings until inspected."
        ),
    },
    "Tomato___Target_Spot": {
        "plant_name": "Tomato",
        "disease_name": "Target spot",
        "is_healthy": False,
        "description": (
            "Target spot (Corynespora cassiicola) forms dark lesions with concentric rings on "
            "leaves, stems, and fruit. It thrives in warm, humid greenhouses and fields with "
            "dense canopies and prolonged wetness."
        ),
        "solution": (
            "1. Apply labeled fungicides at first symptoms; ensure excellent coverage including inner canopy.\n"
            "2. Prune and stake to open the plant; remove heavily infected lower foliage when dry.\n"
            "3. Manage irrigation to shorten leaf wetness duration.\n"
            "4. Sanitize greenhouse structures and tools between crops.\n"
            "5. Remove crop debris after harvest to reduce carryover inoculum."
        ),
        "prevention": (
            "• Avoid excessive nitrogen and overcrowding.\n"
            "• Use clean seed and transplants.\n"
            "• Rotate with non-host crops.\n"
            "• Monitor humidity in tunnels; ventilate proactively."
        ),
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "plant_name": "Tomato",
        "disease_name": "Tomato yellow leaf curl virus (TYLCV)",
        "is_healthy": False,
        "description": (
            "TYLCV is transmitted by sweetpotato whitefly (Bemisia tabaci) and causes severe "
            "leaf curling, yellowing, and stunting. Infected plants set little or no marketable "
            "fruit; management centers on vector and resistant varieties."
        ),
        "solution": (
            "1. Rogue infected plants early in the season to reduce whitefly acquisition.\n"
            "2. Intensively manage whiteflies with labeled insecticides, IGRs, and biological controls per IPM plans.\n"
            "3. Use TYLCV-resistant varieties where fruit type is acceptable.\n"
            "4. In tunnels, use fine screens and double-door entries where cost-effective.\n"
            "5. Remove alternate hosts and weeds that harbor whiteflies."
        ),
        "prevention": (
            "• Produce or buy virus-indexed transplants.\n"
            "• Avoid planting near old tomato fields with high whitefly pressure.\n"
            "• Use reflective mulches to repel whiteflies during establishment.\n"
            "• Monitor with yellow sticky traps to time sprays judiciously."
        ),
    },
    "Tomato___Tomato_mosaic_virus": {
        "plant_name": "Tomato",
        "disease_name": "Tomato mosaic virus (ToMV)",
        "is_healthy": False,
        "description": (
            "ToMV causes mosaic mottling, fern-leaf distortion, and stunting. It spreads "
            "mechanically through handling, tools, clothing, and tobacco products, and may "
            "persist in seed or debris."
        ),
        "solution": (
            "1. Remove and destroy symptomatic plants; do not compost.\n"
            "2. Disinfect tools between plants (e.g., approved quaternary ammonium or bleach solutions per safety guides).\n"
            "3. Avoid smoking or using tobacco near tomatoes.\n"
            "4. Control aphids as secondary helpers of virus spread in some contexts.\n"
            "5. Start with certified seed and clean transplants next season."
        ),
        "prevention": (
            "• Wash hands before working tomatoes; change or sanitize gloves often.\n"
            "• Train crews on hygienic harvest and pruning practices.\n"
            "• Manage weeds that may host viruses or vectors.\n"
            "• Use resistant rootstocks or varieties where they fit your market."
        ),
    },
    "Tomato___healthy": {
        "plant_name": "Tomato",
        "disease_name": "Healthy",
        "is_healthy": True,
        "description": (
            "Tomato foliage appears broadly healthy relative to the disease classes in this "
            "dataset. Continue standard programs for nutrition, irrigation, and pest monitoring "
            "through harvest."
        ),
        "solution": (
            "1. No disease treatment is strictly required from this image alone.\n"
            "2. Maintain consistent soil moisture to reduce blossom-end rot risk.\n"
            "3. Fertilize according to soil tests and growth stage.\n"
            "4. Scout for hornworms, fruitworms, and foliar pathogens weekly in humid weather."
        ),
        "prevention": (
            "• Mulch to reduce splash and conserve moisture.\n"
            "• Stake or cage determinants and indeterminates for airflow.\n"
            "• Rotate tomatoes with unrelated crops where field space allows.\n"
            "• Sanitize trellis materials annually in high-disease gardens."
        ),
    },
}
