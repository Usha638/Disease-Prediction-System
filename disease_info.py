"""
Educational disease information for the 41 labels in the Kaggle Training.csv dataset.

IMPORTANT:
- This is general educational information, not a diagnostic or treatment guide.
- A symptom-based machine-learning prediction is not a medical diagnosis.
- Have a qualified healthcare professional review this content before presenting it as
  authoritative medical information.
"""

DISEASE_INFO = {
    "(vertigo) Paroymsal  Positional Vertigo": {
        "overview": "Benign paroxysmal positional vertigo (BPPV) is a common inner-ear condition that causes brief episodes of spinning dizziness when the head changes position.",
        "causes": "Usually caused by tiny calcium crystals moving into a part of the inner ear where they interfere with balance signals.",
        "symptoms": ["Brief spinning sensation", "Dizziness after turning in bed or looking up", "Nausea", "Balance difficulty"],
        "risk_factors": ["Increasing age", "Previous head injury", "Some inner-ear disorders"],
        "precautions": ["Move slowly during dizzy episodes", "Sit or lie down if balance is affected", "Avoid driving while dizzy"],
        "prevention": "BPPV cannot always be prevented. Reduce head-injury risk and seek assessment for repeated episodes.",
        "doctor": "Seek medical assessment for new or recurring vertigo. Get urgent help for vertigo with weakness, trouble speaking, severe headache, fainting, chest pain, or new hearing loss."
    },
    "AIDS": {
        "overview": "AIDS is the most advanced stage of HIV infection, when the immune system is severely damaged. Effective HIV treatment can prevent progression to AIDS.",
        "causes": "Caused by untreated or inadequately treated infection with the human immunodeficiency virus (HIV).",
        "symptoms": ["May include recurrent infections", "Persistent fever or night sweats", "Unintentional weight loss", "Prolonged diarrhoea", "Symptoms vary widely"],
        "risk_factors": ["HIV exposure through certain sexual or blood contact", "Sharing injection equipment", "Perinatal transmission without prevention or treatment"],
        "precautions": ["Get an HIV test if exposure is possible", "Use condoms and sterile injection equipment", "Take prescribed antiretroviral treatment consistently"],
        "prevention": "HIV prevention includes condoms, PrEP when appropriate, sterile injection equipment, testing, and effective treatment. Treatment that maintains an undetectable viral load prevents sexual transmission.",
        "doctor": "Anyone concerned about HIV exposure should seek prompt medical advice; some prevention medicines must be started within 72 hours. People with HIV need ongoing specialist care."
    },
    "Acne": {
        "overview": "Acne is a common skin condition in which hair follicles become blocked by oil and dead skin cells, causing spots or deeper lumps.",
        "causes": "Involves excess sebum, blocked follicles, inflammation, bacteria, and hormonal influences.",
        "symptoms": ["Blackheads and whiteheads", "Pimples", "Inflamed or painful lumps", "Sometimes scarring"],
        "risk_factors": ["Puberty and hormonal changes", "Family history", "Some medicines and oily skin products"],
        "precautions": ["Use gentle skin cleansing", "Avoid picking or squeezing spots", "Choose non-comedogenic products"],
        "prevention": "Acne cannot always be prevented. Gentle skin care and non-comedogenic products may reduce irritation and blocked pores.",
        "doctor": "Consult a clinician for painful, deep, scarring, or persistent acne, or if it affects emotional wellbeing."
    },
    "Alcoholic hepatitis": {
        "overview": "Alcohol-associated hepatitis is inflammation and liver injury related to heavy alcohol use. It can range from mild to life-threatening.",
        "causes": "Associated with prolonged heavy alcohol consumption, although not everyone who drinks heavily develops it.",
        "symptoms": ["Yellowing of skin or eyes", "Abdominal discomfort", "Nausea or loss of appetite", "Fever", "Weakness"],
        "risk_factors": ["Heavy or prolonged alcohol use", "Existing liver disease", "Poor nutrition"],
        "precautions": ["Stop drinking alcohol and seek medical support", "Do not start medicines or supplements without medical advice", "Follow clinician advice about nutrition and monitoring"],
        "prevention": "Avoiding alcohol or keeping consumption within locally recommended limits reduces alcohol-related liver harm; no amount is risk-free for everyone.",
        "doctor": "Jaundice, abdominal swelling, confusion, vomiting blood, black stools, or severe illness requires urgent medical assessment."
    },
    "Allergy": {
        "overview": "An allergy occurs when the immune system reacts to a normally harmless substance, such as pollen, certain foods, medicines, or insect venom.",
        "causes": "An immune response to an allergen; triggers differ from person to person.",
        "symptoms": ["Sneezing or runny nose", "Itchy or watery eyes", "Hives or itching", "Wheezing or swelling in some reactions"],
        "risk_factors": ["Family history of allergic disease", "Asthma or eczema", "Previous allergic reactions"],
        "precautions": ["Identify and avoid known triggers where possible", "Use prescribed allergy medicines as directed", "Follow an emergency action plan if one has been provided"],
        "prevention": "Avoidance of a known allergen can reduce reactions. Allergy prevention strategies depend on the allergen and individual history.",
        "doctor": "Seek emergency help for difficulty breathing, throat or tongue swelling, collapse, or a rapidly worsening reaction; these may indicate anaphylaxis."
    },
    "Arthritis": {
        "overview": "Arthritis describes conditions that cause inflammation or damage in one or more joints. Different types have different causes and treatments.",
        "causes": "May involve wear-and-tear changes, autoimmune inflammation, crystal deposits, infection, or other conditions.",
        "symptoms": ["Joint pain", "Swelling or stiffness", "Reduced movement", "Warmth around an affected joint"],
        "risk_factors": ["Age", "Joint injury", "Family history", "Some autoimmune or metabolic conditions"],
        "precautions": ["Use gentle, suitable physical activity", "Balance activity with rest", "Follow an individual care plan"],
        "prevention": "Not all arthritis can be prevented. Joint injury prevention, healthy weight, and regular appropriate activity may reduce some risks.",
        "doctor": "Arrange assessment for persistent joint pain or swelling. A suddenly hot, very painful joint with fever needs urgent assessment."
    },
    "Bronchial Asthma": {
        "overview": "Asthma is a long-term condition in which the airways become inflamed and narrowed, causing episodes of breathing difficulty.",
        "causes": "Airway inflammation and sensitivity can be triggered by allergens, infections, exercise, smoke, pollution, or cold air.",
        "symptoms": ["Wheezing", "Coughing", "Chest tightness", "Shortness of breath"],
        "risk_factors": ["Family history of asthma or allergy", "Allergic conditions", "Exposure to smoke or air pollution"],
        "precautions": ["Follow the prescribed asthma action plan", "Use inhalers exactly as instructed", "Avoid personal triggers where possible"],
        "prevention": "Asthma cannot always be prevented. Avoiding tobacco smoke and managing triggers can help reduce attacks.",
        "doctor": "Seek urgent help if breathing is severely difficult, lips look blue or grey, or prescribed reliever treatment is not helping."
    },
    "Cervical spondylosis": {
        "overview": "Cervical spondylosis is age-related wear-and-tear change in the bones and discs of the neck.",
        "causes": "Usually develops gradually as neck discs and joints change with age.",
        "symptoms": ["Neck pain or stiffness", "Headache starting near the neck", "Shoulder discomfort", "Sometimes tingling or weakness in an arm"],
        "risk_factors": ["Increasing age", "Previous neck injury", "Repetitive neck strain"],
        "precautions": ["Maintain comfortable posture", "Take breaks from prolonged fixed positions", "Use exercises recommended by a clinician or physiotherapist"],
        "prevention": "Age-related changes cannot be fully prevented. Good ergonomics, activity, and avoiding neck injuries may help neck function.",
        "doctor": "Seek prompt care for new limb weakness, worsening numbness, problems walking, loss of coordination, or bladder/bowel changes."
    },
    "Chicken pox": {
        "overview": "Chickenpox is a contagious infection caused by the varicella-zoster virus. It typically causes an itchy blister-like rash.",
        "causes": "Infection with varicella-zoster virus, spread through close contact and respiratory particles or fluid from blisters.",
        "symptoms": ["Itchy rash that forms blisters and scabs", "Fever", "Tiredness", "Loss of appetite"],
        "risk_factors": ["No prior immunity or vaccination", "Close contact with an infected person"],
        "precautions": ["Stay away from others until all lesions have crusted", "Avoid scratching", "Ask a clinician about suitable symptom relief"],
        "prevention": "Varicella vaccination is the main way to prevent chickenpox or reduce its severity.",
        "doctor": "Contact a clinician, especially for adults, pregnant people, newborns, or people with weakened immunity. Seek urgent care for breathing difficulty, confusion, severe headache, or infected-looking skin."
    },
    "Chronic cholestasis": {
        "overview": "Cholestasis means that the flow of bile from the liver is reduced or blocked. Chronic cholestasis is a persistent problem and has several possible causes.",
        "causes": "May result from liver diseases, bile-duct disorders, certain medicines, or obstruction of bile flow.",
        "symptoms": ["Itching", "Yellowing of skin or eyes", "Dark urine", "Pale stools", "Fatigue"],
        "risk_factors": ["Underlying liver or bile-duct disease", "Certain medicines", "Some autoimmune conditions"],
        "precautions": ["Avoid alcohol unless a clinician says otherwise", "Do not stop prescribed medicines without advice", "Attend recommended liver tests and follow-up"],
        "prevention": "Prevention depends on the underlying cause; many causes cannot be prevented through lifestyle measures alone.",
        "doctor": "New jaundice, fever with abdominal pain, confusion, or severe illness needs urgent medical assessment."
    },
    "Common Cold": {
        "overview": "The common cold is a usually mild viral infection of the nose and throat.",
        "causes": "Caused by many different respiratory viruses and spread through respiratory droplets, close contact, and contaminated hands or surfaces.",
        "symptoms": ["Runny or blocked nose", "Sneezing", "Sore throat", "Cough", "Mild fever sometimes"],
        "risk_factors": ["Close contact with infected people", "Crowded settings", "Touching the face with unwashed hands"],
        "precautions": ["Rest and drink fluids", "Wash hands regularly", "Cover coughs and sneezes", "Avoid close contact while unwell"],
        "prevention": "Hand hygiene, ventilation, and avoiding close contact with people who are ill can lower the chance of infection.",
        "doctor": "Seek medical advice for difficulty breathing, dehydration, persistent high fever, symptoms that worsen, or symptoms lasting unusually long."
    },
    "Dengue": {
        "overview": "Dengue is a viral infection transmitted to people by infected Aedes mosquitoes. Some cases become severe.",
        "causes": "Infection with dengue virus after the bite of an infected mosquito.",
        "symptoms": ["High fever", "Severe headache or pain behind the eyes", "Muscle and joint pain", "Nausea", "Rash"],
        "risk_factors": ["Living in or travelling to dengue-risk areas", "Mosquito bites", "A previous dengue infection can increase risk of severe disease in a later infection"],
        "precautions": ["Prevent mosquito bites", "Drink fluids and follow medical advice", "Avoid aspirin and ibuprofen unless a clinician specifically advises otherwise"],
        "prevention": "Use mosquito repellents, screens, protective clothing, and remove standing water where mosquitoes breed.",
        "doctor": "Seek urgent care for severe abdominal pain, persistent vomiting, bleeding, breathing difficulty, extreme tiredness, restlessness, or symptoms worsening as fever falls."
    },
    "Diabetes ": {
        "overview": "Diabetes is a group of conditions in which blood glucose levels are too high because the body does not make enough insulin or cannot use it effectively.",
        "causes": "Type 1 involves autoimmune destruction of insulin-producing cells; type 2 involves insulin resistance and progressive insulin-production problems. Other forms also exist.",
        "symptoms": ["Increased thirst", "Frequent urination", "Increased hunger", "Tiredness", "Blurred vision", "Unexplained weight change"],
        "risk_factors": ["Family history", "Excess body weight and inactivity for type 2", "Age and some medical or pregnancy-related factors"],
        "precautions": ["Follow a clinician-guided care plan", "Monitor glucose when advised", "Take prescribed medicines", "Care for feet and attend recommended check-ups"],
        "prevention": "Type 1 diabetes is not currently preventable. Healthy eating, regular activity, and weight management can reduce the risk of type 2 diabetes.",
        "doctor": "Arrange testing for symptoms such as excessive thirst and urination. Vomiting, abdominal pain, deep or rapid breathing, confusion, or severe drowsiness needs emergency care."
    },
    "Dimorphic hemmorhoids(piles)": {
        "overview": "Haemorrhoids (piles) are swollen blood vessels in or around the anus and lower rectum.",
        "causes": "Often associated with increased pressure during bowel movements, constipation, straining, or pregnancy.",
        "symptoms": ["Bright red blood after passing stool", "Itching or irritation", "Discomfort or pain", "A lump near the anus"],
        "risk_factors": ["Constipation or straining", "Low-fibre diet", "Pregnancy", "Prolonged sitting on the toilet"],
        "precautions": ["Increase dietary fibre gradually", "Drink adequate fluids if not medically restricted", "Avoid straining", "Do not delay bowel movements"],
        "prevention": "Fibre-rich foods, adequate fluids, regular activity, and avoiding straining may reduce the risk.",
        "doctor": "Rectal bleeding should be assessed rather than assumed to be piles. Seek urgent care for heavy bleeding, dizziness, severe pain, or black stools."
    },
    "Drug Reaction": {
        "overview": "A drug reaction is an unwanted response to a medicine. Reactions range from mild side effects to serious allergic or toxic reactions.",
        "causes": "Can be caused by a medicine's expected side effects, allergy, interactions, incorrect dosing, or individual sensitivity.",
        "symptoms": ["Rash or itching", "Nausea or diarrhoea", "Swelling", "Dizziness", "Breathing symptoms in severe reactions"],
        "risk_factors": ["Previous reaction to the medicine", "Multiple medicines", "Certain health conditions", "Dose or interaction problems"],
        "precautions": ["Record the medicine and timing of symptoms", "Contact the prescribing clinician or pharmacist", "Do not take another dose until you have obtained advice if a serious reaction is suspected"],
        "prevention": "Tell healthcare professionals about allergies and all medicines or supplements you use. Take medicines only as directed.",
        "doctor": "Difficulty breathing, face or throat swelling, collapse, blistering rash, or sores in the mouth or eyes require emergency care."
    },
    "Fungal infection": {
        "overview": "Fungal infections are caused by fungi and can affect the skin, nails, mouth, or internal organs.",
        "causes": "Exposure to fungi; the specific organism and route depend on the type of infection.",
        "symptoms": ["Itching or scaling skin", "Rash", "Cracked skin", "Nail thickening or colour change", "Symptoms vary by site"],
        "risk_factors": ["Warm, moist skin", "Shared personal items", "Weakened immune system", "Some medicines or medical conditions"],
        "precautions": ["Keep affected areas clean and dry", "Avoid sharing towels or footwear", "Use antifungal treatment only as advised"],
        "prevention": "Dry skin folds and feet well, wear breathable clothing, use footwear in shared wet areas, and avoid sharing personal items.",
        "doctor": "Seek medical advice if the infection spreads, is painful, affects the scalp or nails, keeps returning, or occurs with a weakened immune system."
    },
    "GERD": {
        "overview": "Gastro-oesophageal reflux disease (GERD) occurs when stomach contents repeatedly flow back into the oesophagus and cause troublesome symptoms or complications.",
        "causes": "Often related to weakness or inappropriate relaxation of the lower oesophageal sphincter.",
        "symptoms": ["Heartburn", "Sour or bitter fluid coming into the mouth", "Regurgitation", "Sometimes cough or hoarseness"],
        "risk_factors": ["Excess body weight", "Pregnancy", "Hiatal hernia", "Some foods, medicines, or smoking can worsen symptoms"],
        "precautions": ["Avoid lying down soon after meals", "Identify personal food triggers", "Discuss persistent symptoms with a clinician"],
        "prevention": "Maintaining a healthy weight, avoiding smoking, and not eating close to bedtime may reduce reflux symptoms.",
        "doctor": "Seek urgent care for chest pain, especially with breathlessness or sweating. Difficulty swallowing, vomiting blood, black stools, or unexplained weight loss needs medical assessment."
    },
    "Gastroenteritis": {
        "overview": "Gastroenteritis is inflammation of the stomach and intestines, commonly causing diarrhoea and vomiting.",
        "causes": "Often caused by viruses, bacteria, or parasites acquired through contaminated food, water, or contact.",
        "symptoms": ["Diarrhoea", "Vomiting", "Abdominal cramps", "Nausea", "Sometimes fever"],
        "risk_factors": ["Contaminated food or water", "Poor hand hygiene", "Close contact with an infected person"],
        "precautions": ["Take frequent small amounts of oral rehydration solution when appropriate", "Wash hands carefully", "Prepare and store food safely"],
        "prevention": "Safe drinking water, food hygiene, handwashing, and recommended vaccines where applicable help prevent some causes.",
        "doctor": "Seek care for signs of dehydration, blood in stool, severe abdominal pain, persistent vomiting, high fever, or illness in an infant or vulnerable person."
    },
    "Heart attack": {
        "overview": "A heart attack occurs when blood flow to part of the heart muscle is blocked, causing damage to the heart.",
        "causes": "Most commonly caused by a blood clot blocking a coronary artery, often where fatty plaque has built up.",
        "symptoms": ["Chest pressure, tightness, or pain", "Pain in arm, back, neck, jaw, or stomach", "Shortness of breath", "Sweating", "Nausea or light-headedness"],
        "risk_factors": ["High blood pressure", "High cholesterol", "Smoking", "Diabetes", "Family history", "Increasing age"],
        "precautions": ["Call emergency services immediately if a heart attack is suspected", "Do not drive yourself", "Follow emergency-dispatch instructions"],
        "prevention": "Not all heart attacks can be prevented. Managing blood pressure, cholesterol, diabetes, avoiding tobacco, and regular activity lower risk.",
        "doctor": "A suspected heart attack is an emergency. Call local emergency services immediately; do not wait for symptoms to pass."
    },
    "Hepatitis B": {
        "overview": "Hepatitis B is a viral infection that affects the liver. It can be short-term or become a chronic infection.",
        "causes": "Caused by hepatitis B virus, spread through infected blood and body fluids, including sexual contact and from mother to baby at birth.",
        "symptoms": ["May have no symptoms", "Fatigue", "Nausea", "Abdominal discomfort", "Dark urine or jaundice"],
        "risk_factors": ["Unprotected sexual exposure", "Shared needles or unsterile equipment", "Birth to an infected mother", "Unscreened blood exposure"],
        "precautions": ["Get tested if exposed or at risk", "Avoid sharing razors or needles", "Use barrier protection", "Follow medical monitoring advice"],
        "prevention": "Hepatitis B vaccination is highly effective. Safe injection practices, screened blood, and prevention of perinatal transmission also reduce spread.",
        "doctor": "Seek medical assessment for possible exposure, jaundice, severe abdominal pain, confusion, or known hepatitis B. Testing is needed to confirm infection."
    },
    "Hepatitis C": {
        "overview": "Hepatitis C is a viral infection of the liver. It often causes no early symptoms but can lead to chronic liver disease.",
        "causes": "Caused by hepatitis C virus, mainly spread through contact with infected blood.",
        "symptoms": ["Often no symptoms", "Fatigue", "Nausea", "Abdominal discomfort", "Jaundice in some cases"],
        "risk_factors": ["Sharing injection equipment", "Unsafe medical or tattoo equipment", "Unscreened blood exposure in settings where screening is inadequate"],
        "precautions": ["Get tested if there may have been blood exposure", "Do not share needles or personal items that may carry blood", "Attend follow-up if positive"],
        "prevention": "Avoid blood-to-blood exposure and use sterile equipment. There is currently no widely available vaccine, but effective curative treatment exists.",
        "doctor": "Ask a healthcare professional about testing after possible exposure. A positive screening test needs confirmatory testing and treatment assessment."
    },
    "Hepatitis D": {
        "overview": "Hepatitis D is a liver infection that can occur only in people who also have hepatitis B. It can make liver disease more severe.",
        "causes": "Caused by hepatitis D virus, which requires hepatitis B virus to reproduce.",
        "symptoms": ["May have no symptoms", "Fatigue", "Nausea", "Abdominal pain", "Jaundice"],
        "risk_factors": ["Hepatitis B infection", "Blood exposure through shared injection equipment or unsafe equipment"],
        "precautions": ["People with hepatitis B should ask whether hepatitis D testing is appropriate", "Avoid sharing needles", "Attend liver-care follow-up"],
        "prevention": "Hepatitis B vaccination prevents hepatitis D infection by preventing hepatitis B.",
        "doctor": "People with hepatitis B and worsening liver symptoms should seek medical assessment. Confusion, bleeding, or severe jaundice requires urgent care."
    },
    "Hepatitis E": {
        "overview": "Hepatitis E is a viral liver infection that is often short-lived but can be severe in some people, particularly during pregnancy.",
        "causes": "Usually spread through contaminated water; some types can spread through undercooked meat.",
        "symptoms": ["Fatigue", "Nausea or vomiting", "Abdominal pain", "Dark urine", "Jaundice"],
        "risk_factors": ["Unsafe water or sanitation", "Travel to areas with outbreaks", "Pregnancy, especially later pregnancy, for severe disease risk"],
        "precautions": ["Use safe drinking water", "Cook meat thoroughly", "Seek medical advice if pregnant and exposed or symptomatic"],
        "prevention": "Safe water, sanitation, hand hygiene, and thorough cooking of meat reduce risk.",
        "doctor": "Pregnant people with possible hepatitis E exposure or symptoms should seek prompt medical advice. Jaundice or severe illness needs assessment."
    },
    "Hypertension ": {
        "overview": "Hypertension, or high blood pressure, is persistently raised pressure in the arteries. It often has no noticeable symptoms.",
        "causes": "Usually involves a combination of genetic, lifestyle, age-related, and sometimes kidney or hormonal factors.",
        "symptoms": ["Often no symptoms", "Very high blood pressure may cause headache, visual changes, chest pain, or breathlessness"],
        "risk_factors": ["Increasing age", "Family history", "High-salt diet", "Excess body weight", "Inactivity", "Tobacco use"],
        "precautions": ["Measure blood pressure correctly", "Take prescribed medicines consistently", "Do not stop treatment without medical advice"],
        "prevention": "Regular activity, a balanced lower-salt diet, limiting alcohol, avoiding tobacco, and maintaining a healthy weight can reduce risk.",
        "doctor": "Have blood pressure checked regularly. Very high readings with chest pain, breathlessness, weakness, confusion, or vision changes require emergency assessment."
    },
    "Hyperthyroidism": {
        "overview": "Hyperthyroidism occurs when the thyroid gland produces too much thyroid hormone, speeding up many body functions.",
        "causes": "Common causes include Graves' disease, overactive thyroid nodules, and thyroid inflammation.",
        "symptoms": ["Fast or irregular heartbeat", "Weight loss despite appetite", "Heat intolerance and sweating", "Tremor", "Anxiety or sleep problems"],
        "risk_factors": ["Family history of thyroid disease", "Autoimmune conditions", "Some thyroid medicines or iodine exposures"],
        "precautions": ["Seek testing rather than self-treating", "Take prescribed medicines as directed", "Discuss supplements and medicines with a clinician"],
        "prevention": "Many causes cannot be prevented. Appropriate monitoring and treatment can prevent complications.",
        "doctor": "Seek prompt care for palpitations or unexplained weight loss. Fever, severe agitation, confusion, and very rapid heartbeat can indicate a medical emergency."
    },
    "Hypoglycemia": {
        "overview": "Hypoglycemia means blood glucose is lower than the normal range. It is especially important for people using insulin or certain diabetes medicines.",
        "causes": "May result from diabetes medicines, missed meals, more activity than usual, alcohol, or certain illnesses.",
        "symptoms": ["Shakiness", "Sweating", "Hunger", "Dizziness", "Confusion", "Severe cases may cause seizures or unconsciousness"],
        "risk_factors": ["Insulin or some diabetes medicines", "Delayed or missed meals", "Unplanned strenuous activity", "Alcohol use"],
        "precautions": ["If conscious and able to swallow, follow the clinician-provided low-glucose treatment plan", "Recheck glucose as advised", "Do not give food or drink to someone who is unconscious"],
        "prevention": "Coordinate meals, activity, and diabetes medicines with the care team; carry a fast-acting glucose source if advised.",
        "doctor": "Seizure, unconsciousness, or inability to swallow is an emergency. Repeated low readings should be discussed with the diabetes-care team."
    },
    "Hypothyroidism": {
        "overview": "Hypothyroidism occurs when the thyroid gland does not produce enough thyroid hormone, slowing some body functions.",
        "causes": "Common causes include autoimmune thyroiditis, thyroid surgery or radioactive iodine treatment, and some medicines.",
        "symptoms": ["Tiredness", "Cold intolerance", "Weight gain", "Constipation", "Dry skin", "Slower heart rate"],
        "risk_factors": ["Family history", "Autoimmune disease", "Previous thyroid treatment", "Some medicines"],
        "precautions": ["Get thyroid blood tests when advised", "Take prescribed thyroid medicine consistently", "Do not change the dose without medical advice"],
        "prevention": "Many causes cannot be prevented. Correct diagnosis and appropriate treatment help prevent complications.",
        "doctor": "Consult a clinician for persistent symptoms. Severe drowsiness, confusion, low body temperature, or breathing problems require urgent care."
    },
    "Impetigo": {
        "overview": "Impetigo is a contagious bacterial skin infection that commonly causes sores with golden or honey-coloured crusts.",
        "causes": "Usually caused by Staphylococcus aureus or Streptococcus pyogenes bacteria entering through small breaks in the skin.",
        "symptoms": ["Red sores or blisters", "Oozing fluid", "Honey-coloured crusts", "Itching"],
        "risk_factors": ["Close contact with an infected person", "Scratches or insect bites", "Crowded settings", "Existing skin conditions"],
        "precautions": ["Avoid touching or scratching sores", "Wash hands and keep lesions covered when possible", "Do not share towels or clothing"],
        "prevention": "Good hand hygiene, cleaning minor cuts, and avoiding shared personal items reduce spread.",
        "doctor": "Seek medical advice for suspected impetigo, especially if it spreads, is near the eyes, is accompanied by fever, or affects an infant."
    },
    "Jaundice": {
        "overview": "Jaundice is yellowing of the skin or whites of the eyes due to increased bilirubin. It is a sign, not a disease itself.",
        "causes": "Can result from liver inflammation or damage, blocked bile ducts, or increased breakdown of red blood cells.",
        "symptoms": ["Yellow skin or eyes", "Dark urine", "Pale stools", "Itching", "Sometimes abdominal discomfort"],
        "risk_factors": ["Liver or bile-duct disease", "Certain infections or medicines", "Conditions that break down red blood cells"],
        "precautions": ["Seek medical assessment to identify the cause", "Avoid alcohol until assessed", "Do not take unprescribed medicines or supplements"],
        "prevention": "Prevention depends on the underlying cause; vaccination against hepatitis A and B and avoiding harmful exposures can prevent some causes.",
        "doctor": "New jaundice needs prompt medical assessment. Jaundice with fever, severe abdominal pain, confusion, or bleeding requires urgent care."
    },
    "Malaria": {
        "overview": "Malaria is a potentially serious disease caused by Plasmodium parasites and transmitted through bites of infected female Anopheles mosquitoes.",
        "causes": "Infection with malaria parasites after the bite of an infected mosquito; rarely, transmission occurs through blood.",
        "symptoms": ["Fever", "Chills and sweating", "Headache", "Muscle aches", "Nausea or vomiting"],
        "risk_factors": ["Living in or travelling to malaria-risk areas", "Mosquito exposure", "Lack of appropriate prevention"],
        "precautions": ["Prevent mosquito bites", "Seek prompt testing for fever after possible exposure", "Use travel-prevention medicines only as advised"],
        "prevention": "Insecticide-treated nets, repellents, protective clothing, vector control, and recommended preventive medicines for travellers reduce risk.",
        "doctor": "Fever after travel or residence in a malaria-risk area needs urgent testing. Confusion, seizures, breathing difficulty, or extreme weakness is an emergency."
    },
    "Migraine": {
        "overview": "Migraine is a neurological condition that causes recurring attacks of headache and other symptoms. Attacks can be disabling.",
        "causes": "Involves changes in brain and nerve signalling; the exact cause is not fully understood.",
        "symptoms": ["Moderate or severe headache, often throbbing", "Nausea", "Sensitivity to light or sound", "Sometimes visual or sensory aura"],
        "risk_factors": ["Family history", "Hormonal changes", "Sleep disruption", "Stress", "Individual food or environmental triggers"],
        "precautions": ["Keep a headache diary", "Maintain regular sleep and meals", "Use prescribed medicines as directed"],
        "prevention": "Regular sleep, hydration, meals, exercise, and identifying personal triggers may reduce attacks. Preventive medicines may help some people.",
        "doctor": "A sudden 'worst-ever' headache, weakness, confusion, fever with stiff neck, or new neurological symptoms needs emergency assessment."
    },
    "Osteoarthristis": {
        "overview": "Osteoarthritis is a joint condition involving changes to cartilage, bone, and other joint tissues, often causing pain and stiffness.",
        "causes": "Develops through a combination of age-related joint changes, prior injury, joint loading, and individual biological factors.",
        "symptoms": ["Joint pain during or after activity", "Stiffness after rest", "Reduced flexibility", "Grinding sensation", "Mild swelling"],
        "risk_factors": ["Increasing age", "Previous joint injury", "Excess body weight", "Family history", "Repetitive joint stress"],
        "precautions": ["Choose low-impact activity", "Use clinician-recommended exercises", "Avoid overloading a painful joint", "Discuss pain relief options with a professional"],
        "prevention": "Maintaining a healthy weight, strengthening muscles, and preventing joint injuries may lower risk or delay progression.",
        "doctor": "Seek assessment for persistent pain or loss of function. A suddenly hot, swollen joint or inability to bear weight needs prompt care."
    },
    "Paralysis (brain hemorrhage)": {
        "overview": "Brain haemorrhage is bleeding in or around the brain. It can cause sudden neurological problems, including weakness or paralysis.",
        "causes": "May result from a ruptured blood vessel, high blood pressure, aneurysm, head injury, or blood-thinning medicines.",
        "symptoms": ["Sudden weakness or numbness, often on one side", "Face drooping", "Speech or vision problems", "Severe sudden headache", "Loss of balance or consciousness"],
        "risk_factors": ["High blood pressure", "Aneurysm or blood-vessel abnormalities", "Blood-thinning medicines", "Head injury", "Some substance use"],
        "precautions": ["Treat sudden symptoms as an emergency", "Do not give food, drink, or medicine unless emergency professionals advise", "Note when symptoms began"],
        "prevention": "Blood-pressure control, avoiding tobacco and illicit stimulants, and following medical advice about blood thinners can reduce some risks.",
        "doctor": "Call emergency services immediately for any sudden stroke-like symptom or suspected brain bleed. Do not wait to see whether it improves."
    },
    "Peptic ulcer diseae": {
        "overview": "Peptic ulcer disease involves open sores in the lining of the stomach or the first part of the small intestine.",
        "causes": "Common causes are Helicobacter pylori infection and use of non-steroidal anti-inflammatory drugs (NSAIDs).",
        "symptoms": ["Burning or aching upper abdominal pain", "Bloating", "Nausea", "Feeling full quickly"],
        "risk_factors": ["H. pylori infection", "Regular NSAID use", "Smoking", "Some other medicines or health conditions"],
        "precautions": ["Ask a clinician before using NSAIDs regularly", "Complete prescribed H. pylori treatment", "Avoid smoking"],
        "prevention": "Reducing unnecessary NSAID use, testing and treating H. pylori when indicated, and avoiding smoking can reduce risk.",
        "doctor": "Vomiting blood, black tarry stools, sudden severe abdominal pain, fainting, or marked weakness requires emergency care."
    },
    "Pneumonia": {
        "overview": "Pneumonia is an infection that inflames the air sacs in one or both lungs, which may fill with fluid or pus.",
        "causes": "Can be caused by bacteria, viruses, or fungi.",
        "symptoms": ["Cough, sometimes with phlegm", "Fever or chills", "Shortness of breath", "Chest pain when breathing or coughing", "Fatigue"],
        "risk_factors": ["Very young or older age", "Chronic heart or lung disease", "Weakened immune system", "Smoking"],
        "precautions": ["Seek assessment for breathing symptoms or persistent fever", "Rest and drink fluids if safe", "Take prescribed treatment as directed"],
        "prevention": "Recommended pneumococcal, influenza, COVID-19, and other age- or risk-appropriate vaccines, hand hygiene, and avoiding smoking can reduce risk.",
        "doctor": "Urgent care is needed for severe breathlessness, blue or grey lips, confusion, chest pain, or low oxygen if measured."
    },
    "Psoriasis": {
        "overview": "Psoriasis is a long-term immune-mediated skin condition that causes skin cells to build up too quickly, forming inflamed, scaly patches.",
        "causes": "Involves immune-system activity and genetic susceptibility; it is not contagious.",
        "symptoms": ["Raised red or discoloured patches", "Silvery or flaky scale", "Itching or soreness", "Sometimes nail changes or joint pain"],
        "risk_factors": ["Family history", "Stress", "Skin injury", "Some infections or medicines", "Smoking and excess alcohol can worsen disease"],
        "precautions": ["Moisturise regularly", "Avoid scratching and skin injury", "Use prescribed topical or other treatment as directed"],
        "prevention": "There is no guaranteed way to prevent psoriasis. Managing triggers and following treatment can reduce flares.",
        "doctor": "Consult a clinician for widespread, painful, or infected-looking skin changes. Joint pain or swelling should also be assessed."
    },
    "Tuberculosis": {
        "overview": "Tuberculosis (TB) is an infectious disease caused by Mycobacterium tuberculosis. It most often affects the lungs but can affect other organs.",
        "causes": "Spread through the air when a person with infectious TB disease of the lungs or throat coughs, speaks, or sings.",
        "symptoms": ["Cough lasting several weeks", "Coughing blood or sputum", "Fever", "Night sweats", "Weight loss", "Fatigue"],
        "risk_factors": ["Close contact with infectious TB", "Living or working in crowded settings", "Weakened immune system", "Some chronic illnesses"],
        "precautions": ["Seek testing for persistent cough or known exposure", "Follow infection-control advice", "Complete the full prescribed treatment course"],
        "prevention": "Early detection and complete treatment, good ventilation, and preventive treatment for eligible contacts help reduce spread. BCG vaccination is used in many countries to protect children against severe TB.",
        "doctor": "Seek prompt medical assessment for a prolonged cough, coughing blood, fever with night sweats, or known TB exposure."
    },
    "Typhoid": {
        "overview": "Typhoid fever is a potentially serious systemic infection caused by Salmonella Typhi bacteria.",
        "causes": "Usually spread by consuming food or water contaminated with faeces from an infected person or carrier.",
        "symptoms": ["Prolonged fever", "Headache", "Weakness", "Abdominal pain", "Constipation or diarrhoea"],
        "risk_factors": ["Unsafe food or drinking water", "Poor sanitation", "Travel to areas where typhoid is common"],
        "precautions": ["Use safe drinking water", "Wash hands with soap", "Eat safely prepared food", "Take prescribed antibiotics exactly as directed"],
        "prevention": "Safe water, sanitation, food hygiene, handwashing, and typhoid vaccination for eligible people reduce risk.",
        "doctor": "Seek medical assessment for persistent fever, especially after travel or unsafe food/water exposure. Severe abdominal pain, confusion, or bleeding needs urgent care."
    },
    "Urinary tract infection": {
        "overview": "A urinary tract infection (UTI) is an infection in any part of the urinary system, commonly the bladder.",
        "causes": "Usually caused by bacteria entering the urinary tract, most often from the bowel.",
        "symptoms": ["Burning or pain when urinating", "Frequent or urgent urination", "Lower abdominal discomfort", "Cloudy or bloody urine"],
        "risk_factors": ["Previous UTIs", "Sexual activity", "Urinary tract blockage or catheter", "Pregnancy", "Some medical conditions"],
        "precautions": ["Seek testing for symptoms", "Drink fluids if not medically restricted", "Take prescribed antibiotics exactly as directed"],
        "prevention": "Adequate fluids and avoiding delayed urination may help some people; prevention advice depends on individual risk and recurrent infections.",
        "doctor": "Fever, chills, back or side pain, vomiting, pregnancy, or feeling very unwell with urinary symptoms needs prompt medical assessment."
    },
    "Varicose veins": {
        "overview": "Varicose veins are enlarged, twisted veins, usually in the legs, caused by faulty valves that allow blood to pool.",
        "causes": "Vein valves become weak or damaged, allowing blood to flow backwards and collect in the veins.",
        "symptoms": ["Visible enlarged veins", "Aching or heavy legs", "Ankle swelling", "Itching around veins", "Night cramps"],
        "risk_factors": ["Age", "Family history", "Pregnancy", "Prolonged standing", "Excess body weight"],
        "precautions": ["Walk and move regularly", "Elevate legs when resting if comfortable", "Discuss compression stockings with a clinician"],
        "prevention": "Regular movement, leg elevation, and avoiding long periods of standing or sitting may ease symptoms; varicose veins cannot always be prevented.",
        "doctor": "Seek care for skin changes, ulcers, bleeding, or persistent pain. Sudden one-sided leg swelling or pain, especially with breathlessness, needs urgent assessment."
    },
    "hepatitis A": {
        "overview": "Hepatitis A is a usually short-term viral infection that causes inflammation of the liver.",
        "causes": "Caused by hepatitis A virus, usually spread through contaminated food or water or close contact with an infected person.",
        "symptoms": ["Fatigue", "Nausea", "Abdominal discomfort", "Dark urine", "Jaundice", "Sometimes fever"],
        "risk_factors": ["Unsafe food or water", "Close contact with an infected person", "Travel to areas with higher rates"],
        "precautions": ["Wash hands carefully", "Use safe food and water", "Avoid preparing food for others while infectious and follow public-health advice"],
        "prevention": "Hepatitis A vaccination, handwashing, sanitation, and safe food and water practices help prevent infection.",
        "doctor": "Seek medical advice for jaundice, persistent vomiting, or suspected exposure. Confusion, bleeding, or severe illness requires urgent care."
    }
}


def get_disease_info(disease_name):
    """Return information for a dataset label, tolerating extra spaces."""
    if not disease_name:
        return None

    key = disease_name.strip()
    if key in DISEASE_INFO:
        return DISEASE_INFO[key]

    # Match labels after trimming extra whitespace.
    for disease, info in DISEASE_INFO.items():
        if disease.strip().casefold() == key.casefold():
            return info

    return None
