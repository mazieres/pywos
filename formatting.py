'''
`all_wos_cat` was crawled from: <http://images.webofknowledge.com/WOKRS56B5/help/WOS/hp_subject_category_terms_tasca.html>

Exceptions:
+ with "History & Philosophy of Science", of is capitalized in papers metadatas
+ "Logic" appears

Exceptions were corrected by hand.
'''

all_wos_cat = ['Acoustics', 'Agricultural Economics & Policy', 'Agricultural Engineering', 'Agriculture, Dairy & Animal Science', 'Agriculture, Multidisciplinary', 'Agronomy', 'Allergy', 'Anatomy & Morphology', 'Andrology', 'Anesthesiology', 'Anthropology', 'Archaeology', 'Architecture', 'Area Studies', 'Art', 'Asian Studies', 'Astronomy & Astrophysics', 'Automation & Control Systems', 'Behavioral Sciences', 'Biochemical Research Methods', 'Biochemistry & Molecular Biology', 'Biodiversity Conservation', 'Biology', 'Biophysics', 'Biotechnology & Applied Microbiology', 'Business', 'Business, Finance', 'Cardiac & Cardiovascular Systems', 'Cell & Tissue Engineering', 'Cell Biology', 'Chemistry, Analytical', 'Chemistry, Applied', 'Chemistry, Inorganic & Nuclear', 'Chemistry, Medicinal', 'Chemistry, Multidisciplinary', 'Chemistry, Organic', 'Chemistry, Physical', 'Classics', 'Clinical Neurology', 'Communication', 'Computer Science, Artificial Intelligence', 'Computer Science, Cybernetics', 'Computer Science, Hardware & Architecture', 'Computer Science, Information Systems', 'Computer Science, Interdisciplinary Applications', 'Computer Science, Software Engineering', 'Computer Science, Theory & Methods', 'Construction & Building Technology', 'Criminology & Penology', 'Critical Care Medicine', 'Crystallography', 'Cultural Studies', 'Dance', 'Demography', 'Dentistry, Oral Surgery & Medicine', 'Dermatology', 'Developmental Biology', 'Ecology', 'Economics', 'Education & Educational Research', 'Education, Scientific Disciplines', 'Education, Special', 'Electrochemistry', 'Emergency Medicine', 'Endocrinology & Metabolism', 'Energy & Fuels', 'Engineering, Aerospace', 'Engineering, Biomedical', 'Engineering, Chemical', 'Engineering, Civil', 'Engineering, Electrical & Electronic', 'Engineering, Environmental', 'Engineering, Geological', 'Engineering, Industrial', 'Engineering, Manufacturing', 'Engineering, Marine', 'Engineering, Mechanical', 'Engineering, Multidisciplinary', 'Engineering, Ocean', 'Engineering, Petroleum', 'Entomology', 'Environmental Sciences', 'Environmental Studies', 'Ergonomics', 'Ethics', 'Ethnic Studies', 'Evolutionary Biology', 'Family Studies', 'Film, Radio, Television', 'Fisheries', 'Folklore', 'Food Science & Technology', 'Forestry', 'Gastroenterology & Hepatology', 'Genetics & Heredity', 'Geochemistry & Geophysics', 'Geography', 'Geography, Physical', 'Geology', 'Geosciences, Multidisciplinary', 'Geriatrics & Gerontology', 'Gerontology', 'Health Care Sciences & Services', 'Health Policy & Services', 'Hematology', 'History', 'History & Philosophy Of Science', 'History of Social Sciences', 'Horticulture', 'Hospitality, Leisure, Sport & Tourism', 'Humanities, Multidisciplinary', 'Imaging Science & Photographic Technology', 'Immunology', 'Industrial Relations & Labor', 'Infectious Diseases', 'Information Science & Library Science', 'Instruments & Instrumentation', 'Integrative & Complementary Medicine', 'International Relations', 'Language & Linguistics', 'Law', 'Limnology', 'Linguistics', 'Literary Reviews', 'Literary Theory & Criticism', 'Literature', 'Literature, African, Australian, Canadian', 'Literature, American', 'Literature, British Isles', 'Literature, German, Dutch, Scandinavian', 'Literature, Romance', 'Literature, Slavic', 'Management', 'Marine & Freshwater Biology', 'Materials Science, Biomaterials', 'Materials Science, Ceramics', 'Materials Science, Characterization & Testing', 'Materials Science, Coatings & Films', 'Materials Science, Composites', 'Materials Science, Multidisciplinary', 'Materials Science, Paper & Wood', 'Materials Science, Textiles', 'Mathematical & Computational Biology', 'Mathematics', 'Mathematics, Applied', 'Mathematics, Interdisciplinary Applications', 'Mechanics', 'Medical Ethics', 'Medical Informatics', 'Medical Laboratory Technology', 'Medicine, General & Internal', 'Medicine, Legal', 'Medicine, Research & Experimental', 'Medieval & Renaissance Studies', 'Metallurgy & Metallurgical Engineering', 'Meteorology & Atmospheric Sciences', 'Microbiology', 'Microscopy', 'Mineralogy', 'Mining & Mineral Processing', 'Multidisciplinary Sciences', 'Music', 'Mycology', 'Nanoscience & Nanotechnology', 'Neuroimaging', 'Neurosciences', 'Nuclear Science & Technology', 'Nursing', 'Nutrition & Dietetics', 'Obstetrics & Gynecology', 'Oceanography', 'Oncology', 'Operations Research & Management Science', 'Ophthalmology', 'Optics', 'Ornithology', 'Orthopedics', 'Otorhinolaryngology', 'Paleontology', 'Parasitology', 'Pathology', 'Pediatrics', 'Peripheral Vascular Disease', 'Pharmacology & Pharmacy', 'Philosophy', 'Physics, Applied', 'Physics, Atomic, Molecular & Chemical', 'Physics, Condensed Matter', 'Physics, Fluids & Plasmas', 'Physics, Mathematical', 'Physics, Multidisciplinary', 'Physics, Nuclear', 'Physics, Particles & Fields', 'Physiology', 'Planning & Development', 'Plant Sciences', 'Poetry', 'Political Science', 'Polymer Science', 'Primary Health Care', 'Psychiatry', 'Psychology', 'Psychology, Applied', 'Psychology, Biological', 'Psychology, Clinical', 'Psychology, Developmental', 'Psychology, Educational', 'Psychology, Experimental', 'Psychology, Mathematical', 'Psychology, Multidisciplinary', 'Psychology, Psychoanalysis', 'Psychology, Social', 'Public Administration', 'Public, Environmental & Occupational Health', 'Radiology, Nuclear Medicine & Medical Imaging', 'Rehabilitation', 'Religion', 'Remote Sensing', 'Reproductive Biology', 'Respiratory System', 'Rheumatology', 'Robotics', 'Social Issues', 'Social Sciences, Biomedical', 'Social Sciences, Interdisciplinary', 'Social Sciences, Mathematical Methods', 'Social Work', 'Sociology', 'Soil Science', 'Spectroscopy', 'Sport Sciences', 'Statistics & Probability', 'Substance Abuse', 'Surgery', 'Telecommunications', 'Theater', 'Thermodynamics', 'Toxicology', 'Transplantation', 'Transportation', 'Transportation Science & Technology', 'Tropical Medicine', 'Urban Studies', 'Urology & Nephrology', 'Veterinary Sciences', 'Virology', 'Water Resources', "Women's Studies", 'Zoology', 'Logic']

wos_meaning = { u'AB': u'Abstract', u'AF': u'Author(s) Full Name(s)', u'AR': u'Article Number', u'AU': u'Author(s) Name', u'BA': u'Book Author(s)', u'BE': u'Editors', u'BF': u'Book Author(s)', u'BN': u'ISBN', u'BP': u'Begin Page', u'CA': u'Group Author(s)', u'CL': u'Location - City, Country', u'CR': u'Cited References', u'CT': u'Conference Title', u'CY': u'Date', u'DE': u'Author Keywords', u'DI': u'DOI', u'DT': u'Document Type', u'EM': u'Email Addresse(s)', u'EP': u'End Page', u'FU': u'Funding', u'FX': u'Acknowledgment', u'GA': u'IDS Number', u'GP': u'Book Group Author(s)', u'HO': u'Location - Place', u'ID': u'KeyWords Plus', u'IS': u'Issue', u'JI': u'Source (abrv)', u'LA': u'Language', u'MA': u'Meeting Abstract', u'NR': u'Number of Cited References', u'OI': u'N/A', u'PA': u'Publisher - Address', u'PD': u'Month', u'PG': u'N/A', u'PI': u'Publisher - City', u'PN': u'Part', u'PT': u'N/A', u'PU': u'N/A', u'PY': u'Year', u'RI': u'Author Identifiers', u'RP': u'Reprint Address', u'SC': u'Research Areas', u'SE': u'Book series', u'SI': u'Special Issue', u'SN': u'ISSN', u'SO': u'Source', u'SP': u'Sponsor(s)', u'SU': u'N/A', u'TC': u'Times Cited', u'TI': u'Title', u'UT': u'Accession Number', u'VL': u'Volume', u'WC': u'WOS Categories'}


def unlist(l):
    if isinstance(l, basestring):
        for each in [x.strip() for x in l.split(';')]:
            if each != '': yield each
    if isinstance(l, list):
        for each in l:
            for res in unlist(each):
                yield res

def unwosify(l):
    i = 0
    while i < len(l):
        if l[i][-1] in ['&',',']:
            l[i:i+2] = [' '.join(l[i:i+2])]
        elif '\n' in l[i]:
            l[i:i+2] = [' '.join(l[i:i+2]).replace('\n','')]
        else:
            i += 1
    return l

def check_exceptions(l):
    i = 0
    while i < len(l):
        if ' '.join(l[i:i+2]) in all_wos_cat and i + 1 < len(l):
            l[i:i+2] = [' '.join(l[i:i+2])]
        else:
            i += 1
    return l

def format_wc(l):
    l = check_exceptions(unwosify([_ for _ in unlist(l)]))
    return l

def format_dt(l):
    if isinstance(l, list):
        l = [l[0].strip()]
    elif isinstance(l, basestring):
        l = [x.strip() for x in l.split(';')]
    return l

def format_ti(l):
    if isinstance(l, list):
        l = ' '.join([x.strip() for x in l]).upper()
    elif isinstance(l, basestring):
        l = l.strip().upper()
    return l

def format_sc(l):
    tmp = check_exceptions(unwosify([_ for _ in unlist(l)]))
    if '- Other Topics' in tmp:
        i = tmp.index('- Other Topics')
        tmp[i-1:i+1] = [''.join(tmp[i-1:i+1])]
    l = tmp
    return l

def format_af(l):
    if 'Anonymous' in l:
        l = ['Anonymous'.upper()]
    if isinstance(l, basestring):
        l = [l.strip().upper()]
    if isinstance(l, list):
        l = [x.strip().upper() for x in l]
    return l

def format_cr(l):
    l = [x.strip() for x in l]
    return l

def format_ab(l):
    if isinstance(l, basestring):
        l = l.strip()
    elif isinstance(l, list):
        l = ' '.join([x.strip() for x in l])
    return l

def format_sn(l):
    if isinstance(l, basestring):
        l = l.strip()
    if isinstance(l, list):
        l = l[0].strip()
    return l

def format_de(l):
    l = [x.strip().upper() for x in unlist(l)]
    return l

def format_em(l):
    l = [x.strip().lower() for x in unlist(l)]
    return l

def format_gp(l):
    if isinstance(l, basestring):
        l = l.strip().upper()
    if isinstance(l, list):
        l = l[0].strip().upper()
    return l

def format_ri(l):
    return unwosify([_ for _ in unlist(l)])