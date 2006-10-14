# -*- coding: utf-8  -*-
import config, urllib

__version__='$Id$'

# Parent class for all wiki families

class Family:
    def __init__(self):
        self.name = None
            # Updated from http://meta.wikimedia.org/wiki/Interwiki_sorting_order
        self.alphabetic = [
           'aa','af','ak','als','am','ang','ab','ar','an','roa-rup','frp','as',
           'ast','gn','av','ay','az','bm','bn','zh-min-nan','map-bms','ba','be',
           'bh','bi','bar','bo','bs','br','bg','bxr','ca','cv','ceb','cs','ch',
           'cbk-zam','ny','sn',
           'tum','cho','co','za','cy','da','pdc','de','dv','arc','nv','dz','mh',
           'et','el','eml','en','es','eo','eu','ee','fa','fo','fr','fy','ff','fur','ga',
           'gv','gd','gl','ki','glk','gu','got','ko','ha','haw','hy','hi','ho','hsb','hr',
           'io','ig','ilo','id','ia','ie','iu','ik','os','xh','zu','is','it','he',
           'jv','kl','xal','kn','kr','ka','ks','csb','kk','kk-cn','kk-kz','kk-tr',
           'kw','rw','ky','rn',
           'sw','kv','kg','ht','kj','ku','lad','lbe','lo','la','lv','lb','lij','lt',
           'li','ln','jbo','lg','lmo','hu','mk','mg','ml','mt','mi','mr','mzn','ms',
           'mo','mn','mus','my','nah','na','fj','nl','nds-nl','cr','ne','new','ja','nap',
           'ce','pih','no','nn','nrm','nov','oc','or','om','ng','hz','ug','pa','pi',
           'pam','pag','pap','ps','km','pms','nds','pl','pt','ty','ksh','ro','rmy','rm',
           'qu','ru','war','se','sm','sa','sg','sc','sco','st','tn','sq','ru-sib','scn',
           'si','simple','sd','ss','sk','sl','cu','so','sr','sh','su','fi','sv','tl',
           'ta','roa-tara','tt','te','tet','th','vi','ti','tg','tpi','to','chr','chy','ve',
           'tr','tk','tw','udm','bug','uk','ur','uz','vec','vo','fiu-vro','wa',
           'vls','wo','wuu','ts','ii','yi','yo','zh-yue','diq','zea','bat-smg','zh',
           'zh-tw','zh-cn','zh-classical']
        
        # knownlanguages is the same list but sorted by code
        self.knownlanguages = list(self.alphabetic)
        self.knownlanguages.sort()
        
        self.langs = {}
        
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces = {
            -2: {
                '_default': u'Media',
                'ab': u'Медиа',
                'ar': u'ملف',
                'av': u'Медиа',
                'az': u'Mediya',
                'ba': u'Медиа',
                'bat-smg':u'Medija',
                'be': u'Мэдыя',
                'bg': u'Медия',
                'bs': u'Medija',
                'ce': u'Медиа',
                'cs': u'Média',
                'cv': u'Медиа',
                'el': u'Μέσον',
                'et': u'Meedia',
                'fa': u'مدیا',
                'fo': u'Miðil',
                'ga': u'Meán',
                'he': u'מדיה',
                'hr': u'Mediji',
                'hu': u'Média',
                'is': u'Miðill',
                'ka': u'მედია',
                'kn': u'ಮೀಡಿಯ',
                'ku': u'Medya',
                'kv': u'Медиа',
                'lt': u'Medija',
                'mk': u'Медија',
                'nn': u'Filpeikar',
                'no': u'Medium',
                'pa': u'ਮੀਡੀਆ',
                'rmy':u'Mediya',
                'ru': u'Медиа',
                'sk': u'Médiá',
                'sr': u'Медија',
                'su': u'Média',
                'ta': u'ஊடகம்',
                'te': u'మీడియా',
                'tg': u'Медиа',
                'th': u'สื่อ',
                'udm': u'Медиа',
                'uk': u'Медіа',
                'ur': u'زریعہ',
                'vi': u'Phương tiện',
                'xal': u'Аһар',
                'yi': u'מעדיע',
            },
            -1: {
                '_default': u'Special',
                'ab': u'Служебная',
                'af': u'Spesiaal',
                'als': u'Spezial',
                'an': u'Espezial',
                'ar': u'خاص',
                'ast': u'Especial',
                'av': u'Служебная',
                'ay': u'Special',
                'az': u'Xüsusi',
                'ba': u'Ярҙамсы',
                'bat-smg':u'Specialus',
                'be': u'Спэцыяльныя',
                'bg': u'Специални',
                'bn': u'বিশেষ',
                'br': u'Dibar',
                'bs': u'Posebno',
                'ca': u'Especial',
                'ce': u'Служебная',
                'cs': u'Speciální',
                'csb': u'Specjalnô',
                'cv': u'Ятарлă',
                'cy': u'Arbennig',
                'da': u'Speciel',
                'de': u'Spezial',
                'el': u'Ειδικό',
                'eo': u'Speciala',
                'es': u'Especial',
                'et': u'Eri',
                'eu': u'Aparteko',
                'fa': u'ویژه',
                'fi': u'Toiminnot',
                'fo': u'Serstakur',
                'fur': u'Speciâl',
                'fy': u'Wiki',
                'ga': u'Speisialta',
                'gn': u'Especial',
                'he': u'מיוחד',
                'hi': u'विशेष',
                'hr': u'Posebno',
                'hu': u'Speciális',
                'id': u'Istimewa',
                'is': u'Kerfissíða',
                'it': u'Speciale',
                'ja': u'特別',
                'jv': u'Astamiwa',
                'ka': u'სპეციალური',
                'kn': u'ವಿಶೇಷ',
                'ko': u'특수기능',
                'ku': u'Taybet',
                'kv': u'Служебная',
                'la': u'Specialis',
                'li': u'Speciaal',
                'lt': u'Specialus',
                'mk': u'Специјални',
                'ms': u'Istimewa',
                'nah': u'Especial',
                'nap': u'Speciale',
                'nds': u'Spezial',
                'nds-nl': u'Speciaol',
                'nl': u'Speciaal',
                'nn': u'Spesial',
                'no': u'Spesial',
                'oc': u'Especial',
                'os': u'Сæрмагонд',
                'pa': u'ਖਾਸ',
                'pl': u'Specjalna',
                'pt': u'Especial',
                'qu': u'Especial',
                'rmy':u'Uzalutno',
                'ru': u'Служебная',
                'sc': u'Speciale',
                'sk': u'Špeciálne',
                'sl': u'Posebno',
                'sq': u'Speciale',
                'sr': u'Посебно',
                'su': u'Husus',
                'ta': u'சிறப்பு',
                'te': u'ప్రత్యేక',
                'tg': u'Вижа',
                'th': u'พิเศษ',
                'tr': u'Özel',
                'tt': u'Maxsus',
                'udm': u'Панель',
                'uk': u'Спеціальні',
                'ur': u'خاص',
                'vec':u'Speciale',
                'vi': u'Đặc biệt',
                'wa': u'Sipeciås',
                'xal': u'Көдлхнə',
                'yi': u'באַזונדער',
            },
            0: {
                '_default': None,
            },
            1: {
                '_default': u'Talk',
                'ab': u'Обсуждение',
                'af': u'Bespreking',
                'als': u'Diskussion',
                'an': u'Descusión',
                'ar': u'نقاش',
                'ast': u'Discusión',
                'av': u'Обсуждение',
                'ay': u'Discuter',
                'az': u'Müzakirə',
                'ba': u'Фекер алышыу',
                'bat-smg':u'Aptarimas',
                'be': u'Абмеркаваньне',
                'bg': u'Беседа',
                'bm': u'Discuter',
                'bn': u'আলাপ',
                'br': u'Kaozeal',
                'bs': u'Razgovor',
                'ca': u'Discussió',
                'ce': u'Обсуждение',
                'cs': u'Diskuse',
                'csb': u'Diskùsëjô',
                'cv': u'Сӳтсе явасси',
                'cy': u'Sgwrs',
                'da': u'Diskussion',
                'de': u'Diskussion',
                'el': u'Συζήτηση',
                'eo': u'Diskuto',
                'es': u'Discusión',
                'et': u'Arutelu',
                'eu': u'Eztabaida',
                'fa': u'بحث',
                'fi': u'Keskustelu',
                'fo': u'Kjak',
                'fr': u'Discuter',
                'fur': u'Discussion',
                'fy': u'Oerlis',
                'ga': u'Plé',
                'gn': u'Discusión',
                'he': u'שיחה',
                'hi': u'वार्ता',
                'hr': u'Razgovor',
                'hu': u'Vita',
                'ia': u'Discussion',
                'id': [u'Pembicaraan', u'Bicara'],
                'is': u'Spjall',
                'it': u'Discussione',
                'ja': u'ノート',
                'jv': u'Dhiskusi',
                'ka': u'განხილვა',
                'kn': u'ಚರ್ಚೆಪುಟ',
                'ko': u'토론',
                'ku': u'Nîqaş',
                'kv': u'Обсуждение',
                'la': u'Disputatio',
                'li': u'Euverlik',
                'lt': u'Aptarimas',
                'lv': u'Diskusija',
                'mk': u'Разговор',
                'ms': u'Perbualan',
                'nah': u'Discusión',
                'nap': u'Discussione',
                'nds': u'Diskuschoon',
                'nds-nl': u'Overleg',
                'nl': u'Overleg',
                'nn': u'Diskusjon',
                'no': u'Diskusjon',
                'nv': u"Naaltsoos baa yinísht'į́",
                'oc': u'Discutir',
                'os': u'Дискусси',
                'pa': u'ਚਰਚਾ',
                'pl': u'Dyskusja',
                'pms':u'Discussion',
                'pt': u'Discussão',
                'qu': u'Discusión',
                'ro': u'Discuţie',
                'rmy': [u'Vakyarimata', u'Discuţie'],
                'ru': u'Обсуждение',
                'sc': u'Contièndha',
                'sk': u'Diskusia',
                'sl': u'Pogovor',
                'sq': u'Diskutim',
                'sr': u'Разговор',
                'su': u'Obrolan',
                'sv': u'Diskussion',
                'ta': u'பேச்சு',
                'te': u'చర్చ',
                'tg': u'Баҳс',
                'th': u'พูดคุย',
                'tr': u'Tartışma',
                'tt': u'Bäxäs',
                #'ty': u'Discuter',
                'udm': u'Вераськон',
                'uk': u'Обговорення',
                'ur': u'تبادلۂ خیال',
                'vec':u'Discussion',
                'vi': u'Thảo luận',
                'wa': u'Copene',
                'xal': u'Ухалвр',
                'yi': u'רעדן',
            },
            2: {
                '_default': u'User',
                'ab': u'Участник',
                'af': u'Gebruiker',
                'als': u'Benutzer',
                'an': u'Usuario',
                'ar': u'مستخدم',
                'ast': u'Usuariu',
                'av': u'Участник',
                'ay': u'Utilisateur',
                'az': u'İstifadəçi',
                'ba': u'Ҡатнашыусы',
                'bat-smg':u'Naudotojas',
                'be': u'Удзельнік',
                'bg': u'Потребител',
                'bm': u'Utilisateur',
                'bn': u'ব\u09cdযবহারকারী',
                'br': u'Implijer',
                'bs': u'Korisnik',
                'ca': u'Usuari',
                'ce': u'Участник',
                'cs': u'Uživatel',
                'csb': u'Brëkòwnik',
                'cv': u'Хутшăнакан',
                'cy': u'Defnyddiwr',
                'da': u'Bruger',
                'de': u'Benutzer',
                'el': u'Χρήστης',
                'eo': u'Vikipediisto',
                'es': u'Usuario',
                'et': u'Kasutaja',
                'eu': u'Lankide',
                'fa': u'کاربر',
                'fi': u'Käyttäjä',
                'fo': u'Brúkari',
                'fr': u'Utilisateur',
                'fur': u'Utent',
                'fy': u'Meidogger',
                'ga': u'Úsáideoir',
                'gn': u'Usuario',
                'he': u'משתמש',
                'hi': u'सदस्य',
                'hr': u'Suradnik',
                'ia': u'Usator',
                'id': u'Pengguna',
                'is': u'Notandi',
                'it': u'Utente',
                'ja': u'利用者',
                'jv': u'Panganggo',
                'ka': u'მომხმარებელი',
                'kn': u'ಸದಸ್ಯ',
                'ko': u'사용자',
                'ku': u'Bikarhêner',
                'kv': u'Участник',
                'la': u'Usor',
                'li': u'Gebroeker',
                'lt': u'Naudotojas',
                'lv': u'Lietotājs',
                'mk': u'Корисник',
                'ms': u'Pengguna',
                'nah': u'Usuario',
                'nap': u'Utente',
                'nds': u'Bruker',
                'nds-nl': u'Gebruker',
                'nl': u'Gebruiker',
                'nn': u'Brukar',
                'no': u'Bruker',
                'nv': u"Choinish'įįhí",
                'oc': u'Utilisator',
                'os': u'Архайæг',
                'pa': u'ਮੈਂਬਰ',
                'pl': u'Wikipedysta',
                'pms':u'Utent',
                'pt': u'Usuário',
                'qu': u'Usuario',
                'ro': u'Utilizator',
                'rmy':[u'Jeno', u'Utilizator'],
                'ru': u'Участник',
                'sc': u'Utente',
                'sk': u'Redaktor',
                'sl': u'Uporabnik',
                'sq': u'Përdoruesi',
                'sr': u'Корисник',
                'su': u'Pamaké',
                'sv': u'Användare',
                'ta': u'பயனர்',
                'te': u'సభ్యుడు',
                'tg': u'Корбар',
                'th': u'ผู้ใช' + u'\u0e49',
                'tr': u'Kullanıcı',
                'tt': u'Äğzä',
                #'ty': u'Utilisateur',
                'udm': u'Викиавтор',
                'uk': u'Користувач',
                'ur': u'صارف',
                'vec':u'Utente',
                'vi': u'Thành viên',
                'wa': u'Uzeu',
                'xal': u'Орлцач',
                'yi': u'באַניצער',
            },
            3: {
                '_default': u'User talk',
                'ab': u'Обсуждение участника',
                'af': u'Gebruikerbespreking',
                'als': u'Benutzer Diskussion',
                'an': u'Descusión usuario',
                'ar': u'نقاش المستخدم',
                'ast': u'Usuariu discusión',
                'av': u'Обсуждение участника',
                'ay': u'Discussion Utilisateur',
                'az': u'İstifadəçi müzakirəsi',
                'ba': u'Ҡатнашыусы м-н фекер алышыу',
                'bat-smg':u'Naudotojo aptarimas',
                'be': u'Гутаркі ўдзельніка',
                'bg': u'Потребител беседа',
                'bm': u'Discussion Utilisateur',
                'bn': u'ব্যবহারকারী আলাপ',
                'br': u'Kaozeadenn Implijer',
                'bs': u'Razgovor sa korisnikom',
                'ca': u'Usuari Discussió',
                'ce': u'Обсуждение участника',
                'cs': u'Uživatel diskuse',
                'csb': u'Diskùsëjô brëkòwnika',
                'cv': u'Хутшăнаканăн канашлу страници',
                'cy': u'Sgwrs Defnyddiwr',
                'da': u'Bruger diskussion',
                'de': u'Benutzer Diskussion',
                'el': u'Συζήτηση χρήστη',
                'eo': u'Vikipediista diskuto',
                'es': u'Usuario Discusión',
                'et': u'Kasutaja arutelu',
                'eu': u'Lankide eztabaida',
                'fa': u'بحث کاربر',
                'fi': u'Keskustelu käyttäjästä',
                'fo': u'Brúkari kjak',
                'fr': u'Discussion Utilisateur',
                'fur': u'Discussion utent',
                'fy': u'Meidogger oerlis',
                'ga': u'Plé úsáideora',
                'gn': u'Usuario Discusión',
                'he': u'שיחת משתמש',
                'hi': u'सदस्य वार्ता',
                'hr': u'Razgovor sa suradnikom',
                'hu': u'User vita',
                'ia': u'Discussion Usator',
                'id': u'Pembicaraan Pengguna',
                'is': u'Notandaspjall',
                'it': u'Discussioni utente',
                'ja': u'利用者‐会話',
                'jv': u'Dhiskusi Panganggo',
                'ka': u'მომხმარებელი განხილვა',
                'kn': u'ಸದಸ್ಯರ ಚರ್ಚೆಪುಟ',
                'ko': u'사용자토론',
                'ku': u'Bikarhêner nîqaş',
                'kv': u'Обсуждение участника',
                'la': u'Disputatio Usoris',
                'li': u'Euverlik gebroeker',
                'lt': u'Naudotojo aptarimas',
                'lv': u'Lietotāja diskusija',
                'mk': u'Разговор со корисник',
                'ms': u'Perbualan Pengguna',
                'nah': u'Usuario Discusión',
                'nap': u'Discussioni utente',
                'nds': u'Bruker Diskuschoon',
                'nds-nl': u'Overleg gebruker',
                'nl': u'Overleg gebruiker',
                'nn': u'Brukardiskusjon',
                'no': u'Brukerdiskusjon',
                'nv': u"Choinish'įįhí baa yinísht'į́",
                'oc': u'Discutida Utilisator',
                'os': u'Архайæджы дискусси',
                'pa': u'ਮੈਂਬਰ ਚਰਚਾ',
                'pl': u'Dyskusja Wikipedysty',
                'pms':u'Ciaciarade',
                'pt': u'Usuário Discussão',
                'qu': u'Usuario Discusión',
                'rmy':[u'Jeno vakyarimata', u'Discuţie Utilizator'],
                'ro': u'Discuţie Utilizator',
                'ru': u'Обсуждение участника',
                'sc': u'Utente discussioni',
                'sk': u'Diskusia s redaktorom',
                'sl': u'Uporabniški pogovor',
                'sq': u'Përdoruesi diskutim',
                'sr': u'Разговор са корисником',
                'su': u'Obrolan pamaké',
                'sv': u'Användardiskussion',
                'ta': u'பயனர் பேச்சு',
                'te': u'సభ్యునిపై చర్చ',
                'tg': u'Баҳси корбар',
                'th': u'คุยกับผู้ใช้',
                'tr': u'Kullanıcı mesaj',
                'tt': u'Äğzä bäxäse',
                #'ty': u'Discussion Utilisateur',
                'udm': u'Викиавтор сярысь вераськон',
                'uk': u'Обговорення користувача',
                'ur': u'تبادلۂ خیال صارف',
                'vec':u'Discussion utente',
                'vi': u'Thảo luận Thành viên',
                'wa': u'Uzeu copene',
                'xal': u'Орлцачна тускар ухалвр',
                'yi': u'באַניצער רעדן',
            },
            4: {
                '_default': u'Project',
            },
            5: {
                '_default': u'Project talk',
            },
            6: {
                '_default': u'Image',
                'ab': u'Изображение',
                'af': u'Beeld',
                'als': u'Bild',
                'an': u'Imachen',
                'ar': u'صورة',
                'ast': u'Imaxen',
                'av': u'Изображение',
                'az': u'Şəkil',
                'ba': u'Рәсем',
                'bat-smg':u'Vaizdas',
                'be': u'Выява',
                'bg': u'Картинка',
                'bn': u'চিত্র',
                'br': u'Skeudenn',
                'bs': u'Slika',
                'ca': u'Imatge',
                'cbs': u'Òbrôzk',
                'ce': u'Изображение',
                'cs': u'Soubor',
                'csb': u'Òbrôzk',
                'cv': u'Ӳкерчĕк',
                'cy': u'Delwedd',
                'da': u'Billede',
                'de': u'Bild',
                'el': u'Εικόνα',
                'eo': u'Dosiero',
                'es': u'Imagen',
                'et': u'Pilt',
                'eu': u'Irudi',
                'fa': u'تصویر',
                'fi': u'Kuva',
                'fo': u'Mynd',
                'fur': u'Figure',
                'fy': u'Ofbyld',
                'ga': u'Íomhá',
                'gn': u'Imagen',
                'he': u'תמונה',
                'hi': u'चित्र',
                'hr': u'Slika',
                'hu': u'Kép',
                'ia': u'Imagine',
                'id': [u'Berkas', u'Gambar'],
                'is': u'Mynd',
                'it': u'Immagine',
                'ja': u'画像',
                'jv': u'Gambar',
                'ka': u'სურათი',
                'kn': u'ಚಿತ್ರ',
                'ko': u'그림',
                'ku': u'Wêne',
                'kv': u'Изображение',
                'la': u'Imago',
                'li': u'Aafbeilding',
                'lt': u'Vaizdas',
                'lv': u'Attēls',
                'mk': u'Слика',
                'ms': u'Imej',
                'nah': u'Imagen',
                'nap': u'Immagine',
                'nds': u'Bild',
                'nds-nl': u'Ofbeelding',
                'nl': u'Afbeelding',
                'nn': u'Fil',
                'no': u'Bilde',
                'nv': u"E'elyaaígíí",
                'oc': u'Imatge',
                'os': u'Ныв',
                'pa': u'ਤਸਵੀਰ',
                'pl': u'Grafika',
                'pms':u'Figura',
                'pt': u'Imagem',
                'qu': u'Imagen',
                'rmy':[u'Chitro', u'Imagine'],
                'ro': u'Imagine',
                'ru': u'Изображение',
                'sc': u'Immàgini',
                'sk': u'Obrázok',
                'sl': u'Slika',
                'sq': u'Figura',
                'sr': u'Слика',
                'su': u'Gambar',
                'sv': u'Bild',
                'ta': u'படிமம்',
                'te': u'బొమ్మ',
                'tg': u'Акс',
                'th': u'ภาพ',
                'tr': u'Resim',
                'tt': u'Räsem',
                'udm': u'Суред',
                'uk': u'Зображення',
                'ur': u'تصویر',
                'vec':u'Imagine',
                'vi': u'Hình',
                'wa': u'Imådje',
                'xal': u'Зург',
                'yi': u'בילד',
            },
            7: {
                '_default': u'Image talk',
                'ab': u'Обсуждение изображения',
                'af': u'Beeldbespreking',
                'als': u'Bild Diskussion',
                'an': u'Descusión imachen',
                'ar': u'نقاش الصورة',
                'ast': u'Imaxen discusión',
                'av': u'Обсуждение изображения',
                'ay': u'Discussion Image',
                'az': u'Şəkil müzakirəsi',
                'ba': u'Рәсем б-са фекер алышыу',
                'bat-smg':u'Vaizdo aptarimas',
                'be': u'Абмеркаваньне выявы',
                'bg': u'Картинка беседа',
                'bm': u'Discussion Image',
                'bn': u'চিত্র আলাপ',
                'br': u'Kaozeadenn Skeudenn',
                'bs': u'Razgovor o slici',
                'ca': u'Imatge Discussió',
                'ce': u'Обсуждение изображения',
                'cs': u'Soubor diskuse',
                'csb': u'Diskùsëjô òbrôzków',
                'cv': u'Ӳкерчĕке сӳтсе явмалли',
                'cy': u'Sgwrs Delwedd',
                'da': u'Billede diskussion',
                'de': u'Bild Diskussion',
                'el': u'Συζήτηση εικόνας',
                'eo': u'Dosiera diskuto',
                'es': u'Imagen Discusión',
                'et': u'Pildi arutelu',
                'eu': u'Irudi eztabaida',
                'fa': u'بحث تصویر',
                'fi': u'Keskustelu kuvasta',
                'fo': u'Mynd kjak',
                'fr': u'Discussion Image',
                'fur': u'Discussion figure',
                'fy': u'Ofbyld oerlis',
                'ga': u'Plé íomhá',
                'gn': u'Imagen Discusión',
                'he': u'שיחת תמונה',
                'hi': u'चित्र वार्ता',
                'hr': u'Razgovor o slici',
                'hu': u'Kép vita',
                'ia': u'Discussion Imagine',
                'id': [u'Pembicaraan Berkas', u'Pembicaraan Gambar'],
                'is': u'Myndaspjall',
                'it': u'Discussioni immagine',
                'ja': u'画像‐ノート',
                'jv': u'Dhiskusi Gambar',
                'ka': u'სურათი განხილვა',
                'kn': u'ಚಿತ್ರ ಚರ್ಚೆಪುಟ',
                'ko': u'그림토론',
                'ku': u'Wêne nîqaş',
                'kv': u'Обсуждение изображения',
                'la': u'Disputatio Imaginis',
                'li': u'Euverlik afbeelding',
                'lt': u'Vaizdo aptarimas',
                'lv': u'Attēla diskusija',
                'mk': u'Разговор за слика',
                'ms': u'Imej Perbualan',
                'nah': u'Imagen Discusión',
                'nap': u'Discussioni immagine',
                'nds': u'Bild Diskuschoon',
                'nds-nl': u'Overleg ofbeelding',
                'nl': u'Overleg afbeelding',
                'nn': u'Fildiskusjon',
                'no': u'Bildediskusjon',
                'nv': u"E'elyaaígíí baa yinísht'į́",
                'oc': u'Discutida Imatge',
                'os': u'Нывы тыххæй дискусси',
                'pa': u'ਤਸਵੀਰ ਚਰਚਾ',
                'pl': u'Dyskusja grafiki',
                'pms':u'Discussion dla figura',
                'pt': u'Imagem Discussão',
                'qu': u'Imagen Discusión',
                'rmy':[u'Chitro vakyarimata', u'Discuţie Imagine'],
                'ro': u'Discuţie Imagine',
                'ru': u'Обсуждение изображения',
                'sc': u'Immàgini contièndha',
                'sk': u'Diskusia k obrázku',
                'sl': u'Pogovor o sliki',
                'sq': u'Figura diskutim',
                'sr': u'Разговор о слици',
                'su': u'Obrolan gambar',
                'sv': u'Bilddiskussion',
                'ta': [u'படிமப் பேச்சு', u'உருவப் பேச்சு'],
                'te': u'బొమ్మపై చర్చ',
                'tg': u'Баҳси акс',
                'th': u'คุยเรื่องภาพ',
                'tr': u'Resim tartışma',
                'tt': u'Räsem bäxäse',
                #'ty': u'Discussion Image',
                'udm': u'Суред сярысь вераськон',
                'uk': u'Обговорення зображення',
                'ur': u'تبادلۂ خیال تصویر',
                'vec':u'Discussion imagine',
                'vi': u'Thảo luận Hình',
                'wa': u'Imådje copene',
                'xal': u'Зургин тускар ухалвр',
                'yi': u'בילד רעדן',
            },
            8: {
                '_default': u'MediaWiki',
                'ar': u'ميدياويكي',
                'az': u'MediyaViki',
                'bg': u'МедияУики',
                'bs': u'MedijaViki',
                'cy': u'MediaWici',
                'fa': u'مدیاویکی',
                'fo': u'MidiaWiki',
                'he': u'מדיה ויקי',
                'is': u'Melding',
                'ka': u'მედიავიკი',
                'kn': u'ಮೀಡಿಯವಿಕಿ',
                'mk': u'МедијаВики',
                'oc': u'Mediaòiqui',
                'pa': u'ਮੀਡੀਆਵਿਕਿ',
                'rmy':u'MediyaViki',
                'sr': u'МедијаВики',
                'ta': u'மீடியாவிக்கி',
                'te': u'మీడియావికీ',
                'tg': u'Медиавики',
                'th': u'มีเดียวิกิ',
                'tr': u'MedyaViki',
                'ur': u'میڈیاوک',
                'yi': u'מעדיעװיקי',
            },
            9: {
                '_default': u'MediaWiki talk',
                'ab': u'Обсуждение MediaWiki',
                'af': u'MediaWikibespreking',
                'als': u'MediaWiki Diskussion',
                'an': u'Descusión MediaWiki',
                'ar': u'نقاش ميدياويكي',
                'ast': u'MediaWiki discusión',
                'av': u'Обсуждение MediaWiki',
                'ay': u'Discussion MediaWiki',
                'az': u'MediyaViki müzakirəsi',
                'ba': u'MediaWiki б-са фекер алышыу',
                'bat-smg':u'MediaWiki aptarimas',
                'be': u'Абмеркаваньне MediaWiki',
                'bg': u'МедияУики беседа',
                'bm': u'Discussion MediaWiki',
                'bn': u'MediaWiki আলাপ',
                'br': u'Kaozeadenn MediaWiki',
                'bs': u'Razgovor o MedijaVikiju',
                'ca': u'MediaWiki Discussió',
                'ce': u'Обсуждение MediaWiki',
                'cs': u'MediaWiki diskuse',
                'csb': u'Diskùsëjô MediaWiki',
                'cv': u'MediaWiki сӳтсе явмалли',
                'cy': u'Sgwrs MediaWici',
                'da': u'MediaWiki diskussion',
                'de': u'MediaWiki Diskussion',
                'eo': u'MediaWiki diskuto',
                'es': u'MediaWiki Discusión',
                'et': u'MediaWiki arutelu',
                'eu': u'MediaWiki eztabaida',
                'fa': u'بحث مدیاویکی',
                'fo': u'MidiaWiki kjak',
                'fr': u'Discussion MediaWiki',
                'fur': u'Discussion MediaWiki',
                'fy': u'MediaWiki oerlis',
                'ga': u'Plé MediaWiki',
                'gn': u'MediaWiki Discusión',
                'he': u'שיחת מדיה ויקי',
                'hr': u'MediaWiki razgovor',
                'hu': u'MediaWiki vita',
                'ia': u'Discussion MediaWiki',
                'id': u'Pembicaraan MediaWiki',
                'is': u'Meldingarspjall',
                'it': u'Discussioni MediaWiki',
                'ja': u'MediaWiki‐ノート',
                'jv': u'Dhiskusi MediaWiki',
                'ka': u'მედიავიკი განხილვა',
                'kn': u'ಮೀಡೀಯವಿಕಿ ಚರ್ಚೆ',
                'ko': u'MediaWiki토론',
                'ku': u'MediaWiki nîqaş',
                'kv': u'Обсуждение MediaWiki',
                'la': u'Disputatio MediaWiki',
                'li': u'Euverlik MediaWiki',
                'lt': u'MediaWiki aptarimas',
                'lv': u'MediaWiki diskusija',
                'mk': u'Разговор за МедијаВики',
                'ms': u'MediaWiki Perbualan',
                'nah': u'MediaWiki Discusión',
                'nap': u'Discussioni MediaWiki',
                'nds': u'MediaWiki Diskuschoon',
                'nds-nl': u'Overleg MediaWiki',
                'nl': u'Overleg MediaWiki',
                'nn': u'MediaWiki-diskusjon',
                'no': u'MediaWiki-diskusjon',
                'nv': u"MediaWiki baa yinísht'į́",
                'oc': u'Discutida Mediaòiqui',
                'os': u'Дискусси MediaWiki',
                'pa': u'ਮੀਡੀਆਵਿਕਿ ਚਰਚਾ',
                'pl': u'Dyskusja MediaWiki',
                'pms':u'Discussion dla MediaWiki',
                'pt': u'MediaWiki Discussão',
                'qu': u'MediaWiki Discusión',
                'rmy':[u'MediyaViki vakyarimata', u'Discuţie MediaWiki'],
                'ro': u'Discuţie MediaWiki',
                'ru': u'Обсуждение MediaWiki',
                'sk': u'Diskusia k MediaWiki',
                'sl': u'Pogovor o MediaWiki',
                'sq': u'MediaWiki diskutim',
                'sr': u'Разговор о МедијаВикију',
                'su': u'Obrolan MediaWiki',
                'sv': u'MediaWiki-diskussion',
                'ta': u'மீடியாவிக்கி பேச்சு',
                'te': u'మీడియావికీ చర్చ',
                'tg': u'Баҳси медиавики',
                'th': u'คุยเรื่องมีเดียวิกิ',
                'tr': u'MedyaViki tartışma',
                'tt': u'MediaWiki bäxäse',
                #'ty': u'Discussion MediaWiki',
                'udm': u'MediaWiki сярысь вераськон',
                'uk': u'Обговорення MediaWiki',
                'ur': u'تبادلۂ خیال میڈیاوک',
                'vec':u'Discussion MediaWiki',
                'vi': u'Thảo luận MediaWiki',
                'wa': u'MediaWiki copene',
                'xal': u'MediaWiki тускар ухалвр',
                'yi': u'מעדיעװיקי רעדן',          
            },
            10: {
                '_default':u'Template',
                'ab': u'Шаблон',
                'af': u'Sjabloon',
                'als': u'Vorlage',
                'an': u'Plantilla',
                'ar': u'قالب',
                'ast': u'Plantilla',
                'av': u'Шаблон',
                'ay': u'Modèle',
                'az': u'Şablon',
                'ba': u'Ҡалып',
                'bat-smg':u'Šablonas',
                'be': u'Шаблён',
                'bg': u'Шаблон',
                'bm': u'Modèle',
                'br': u'Patrom',
                'bs': u'Šablon',
                'ca': u'Plantilla',
                'cbs': u'Szablóna',
                'ce': u'Шаблон',
                'cs': u'Šablona',
                'csb': u'Szablóna',
                'cv': u'Шаблон',
                'cy': u'Nodyn',
                'da': u'Skabelon',
                'de': u'Vorlage',
                'el': u'Πρότυπο',
                'eo': u'Ŝablono',
                'es': u'Plantilla',
                'et': u'Mall',
                'eu': u'Txantiloi',
                'fa': u'الگو',
                'fi': u'Malline',
                'fo': u'Fyrimynd',
                'fr': u'Modèle',
                'fur': u'Model',
                'fy': u'Berjocht',
                'ga': u'Teimpléad',
                'gn': u'Plantilla',
                'he': u'תבנית',
                'hr': u'Predložak',
                'hu': u'Sablon',
                'ia': u'Patrono',
                'id': u'Templat',
                'is': u'Snið',
                'jv': u'Cithakan',
                'ka': u'თარგი',
                'kn': u'ಟೆಂಪ್ಲೇಟು',
                'ko': u'틀',
                'ku': u'Şablon',
                'kv': u'Шаблон',
                'la': u'Formula',
                'li': u'Sjabloon',
                'lt': u'Šablonas',
                'lv': u'Veidne',
                'mk': u'Шаблон',
                'ms': u'Templat',
                'nah': u'Plantilla',
                'nds': u'Vörlaag',
                'nds-nl': u'Sjabloon',
                'nl': u'Sjabloon',
                'nn': u'Mal',
                'no': u'Mal',
                'oc': u'Modèl',
                'os': u'Шаблон',
                'pa': u'ਨਮੂਨਾ',
                'pl': u'Szablon',
                'pms': u'Stamp',
                'pt': u'Predefinição',
                'qu': u'Plantilla',
                'rmy':[u'Sikavno', u'Format'],
                'ro': u'Format',
                'ru': u'Шаблон',
                'sk': u'Šablóna',
                'sl': u'Predloga',
                'sq': u'Stampa',
                'sr': u'Шаблон',
                'su': u'Citakan',
                'sv': u'Mall',
                'ta': u'வார்ப்புரு',
                'te': u'మూస',
                'tg': u'Шаблон',
                'th': u'แม่แบบ',
                'tr': u'Şablon',
                'tt': u'Ürnäk',
                #'ty': u'Modèle',
                'udm': u'Шаблон',
                'uk': u'Шаблон',
                'ur': u'سانچہ',
                'vi': u'Tiêu bản',
                'wa': u'Modele',
                'xal': u'Зура',
                'yi': u'מוסטער',
            },
            11: {
                '_default': u'Template talk',
                'ab': u'Обсуждение шаблона',
                'af': u'Sjabloonbespreking',
                'als': u'Vorlage Diskussion',
                'an': u'Descusión plantilla',
                'ar': u'نقاش قالب',
                'ast': u'Plantilla discusión',
                'av': u'Обсуждение шаблона',
                'ay': u'Discussion Modèle',
                'az': u'Şablon müzakirəsi',
                'ba': u'Ҡалып б-са фекер алышыу',
                'bat-smg':u'Šablono aptarimas',
                'be': u'Абмеркаваньне шаблёну',
                'bg': u'Шаблон беседа',
                'bm': u'Discussion Modèle',
                'br': u'Kaozeadenn Patrom',
                'bs': u'Razgovor o šablonu',
                'ca': u'Plantilla Discussió',
                'ce': u'Обсуждение шаблона',
                'cs': u'Šablona diskuse',
                'csb': u'Diskùsëjô Szablónë',
                'cv': u'Шаблона сӳтсе явмалли',
                'cy': u'Sgwrs Nodyn',
                'da': u'Skabelon diskussion',
                'de': u'Vorlage Diskussion',
                'el': u'Συζήτηση προτύπου',
                'eo': u'Ŝablona diskuto',
                'es': u'Plantilla Discusión',
                'et': u'Malli arutelu',
                'eu': u'Txantiloi eztabaida',
                'fa': u'بحث الگو',
                'fi': u'Keskustelu mallineesta',
                'fo': u'Fyrimynd kjak',
                'fr': u'Discussion Modèle',
                'fur': u'Discussion model',
                'fy': u'Berjocht oerlis',
                'ga': u'Plé teimpléid',
                'gn': u'Plantilla Discusión',
                'he': u'שיחת תבנית',
                'hr': u'Razgovor o predlošku',
                'hu': u'Sablon vita',
                'ia': u'Discussion Patrono',
                'id': u'Pembicaraan Templat',
                'is': u'Sniðaspjall',
                'it': u'Discussioni template',
                'ja': u'Template‐ノート',
                'jv': u'Dhiskusi Cithakan',
                'ka': u'თარგი განხილვა',
                'kn': u'ಟೆಂಪ್ಲೇಟು ಚರ್ಚೆ',
                'ko': u'틀토론',
                'ku': u'Şablon nîqaş',
                'kv': u'Обсуждение шаблона',
                'la': u'Disputatio Formulae',
                'li': u'Euverlik sjabloon',
                'lt': u'Šablono aptarimas',
                'lv': u'Veidnes diskusija',
                'mk': u'Разговор за шаблон',
                'ms': u'Perbualan Templat',
                'nah': u'Plantilla Discusión',
                'nap': u'Discussioni template',
                'nds': u'Vörlaag Diskuschoon',
                'nds-nl': u'Overleg sjabloon',
                'nl': u'Overleg sjabloon',
                'nn': u'Maldiskusjon',
                'no': u'Maldiskusjon',
                'oc': u'Discutida Modèl',
                'os': u'Шаблоны тыххæй дискусси',
                'pa': u'ਨਮੂਨਾ ਚਰਚਾ',
                'pl': u'Dyskusja szablonu',
                'pms':u'Discussion dlë stamp',
                'pt': u'Predefinição Discussão',
                'qu': u'Plantilla Discusión',
                'rmy':[u'Sikavno vakyarimata', u'Discuţie Format'],
                'ro': u'Discuţie Format',
                'ru': u'Обсуждение шаблона',
                'sk': u'Diskusia k šablóne',
                'sl': u'Pogovor o predlogi',
                'sq': u'Stampa diskutim',
                'sr': u'Разговор о шаблону',
                'su': u'Obrolan citakan',
                'sv': u'Malldiskussion',
                'ta': u'வார்ப்புரு பேச்சு',
                'te': u'మూస చర్చ',
                'tg': u'Баҳси шаблон',
                'th': u'คุยเรื่องแม่แบบ',
                'tr': u'Şablon tartışma',
                'tt': u'Ürnäk bäxäse',
                #'ty': u'Discussion Modèle',
                'udm': u'Шаблон сярысь вераськон',
                'uk': u'Обговорення шаблону',
                'ur': u'تبادلۂ خیال سانچہ',
                'vec':u'Discussion template',
                'vi': u'Thảo luận Tiêu bản',
                'wa': u'Modele copene',
                'xal': u'Зуран тускар ухалвр',
                'yi': u'מוסטער רעדן',
            },
            12: {
                '_default': u'Help',
                'ab': u'Справка',
                'af': u'Hulp',
                'als': u'Hilfe',
                'an': u'Aduya',
                'ar': u'مساعدة',
                'ast': u'Ayuda',
                'av': u'Справка',
                'ay': u'Aide',
                'az': u'Kömək',
                'ba': u'Белешмә',
                'bat-smg':u'Pagalba',
                'be': u'Дапамога',
                'bg': u'Помощ',
                'bm': u'Aide',
                'br': u'Skoazell',
                'bs': u'Pomoć',
                'ca': u'Ajuda',
                'cbs': u'Pòmòc',
                'ce': u'Справка',
                'cs': u'Nápověda',
                'csb': u'Pòmòc',
                'cv': u'Пулăшу',
                'cy': u'Cymorth',
                'da': u'Hjælp',
                'de': u'Hilfe',
                'el': u'Βοήθεια',
                'eo': u'Helpo',
                'es': u'Ayuda',
                'et': u'Juhend',
                'fa': u'راهنما',
                'fi': u'Ohje',
                'fo': u'Hjálp',
                'fr': u'Aide',
                'fur': u'Jutori',
                'fy': u'Hulp',
                'ga': u'Cabhair',
                'gn': u'Ayuda',
                'he': u'עזרה',
                'hr': u'Pomoć',
                'hu': u'Segítség',
                'ia': u'Adjuta',
                'id': u'Bantuan',
                'is': u'Hjálp',
                'it': u'Aiuto',
                'jv': u'Pitulung',
                'ka': u'დახმარება',
                'kn': u'ಸಹಾಯ',
                'ko': u'도움말',
                'ku': u'Alîkarî',
                'kv': u'Справка',
                'la': u'Auxilium',
                'lt': u'Pagalba',
                'lv': u'Palīdzība',
                'mk': u'Помош',
                'ms': u'Bantuan',
                'nah': u'Ayuda',
                'nap': u'Aiuto',
                'nds': u'Hülp',
                'nn': u'Hjelp',
                'no': u'Hjelp',
                'nv': u"Aná'álwo'",
                'oc': u'Ajuda',
                'os': u'Æххуыс',
                'pa': u'ਮਦਦ',
                'pl': u'Pomoc',
                'pms':u'Agiut',
                'pt': u'Ajuda',
                'qu': u'Ayuda',
                'rmy':[u'Zhutipen', u'Ajutor'],
                'ro': u'Ajutor',
                'ru': u'Справка',
                'sk': u'Pomoc',
                'sl': u'Pomoč',
                'sq': u'Ndihmë',
                'sr': u'Помоћ',
                'su': u'Pitulung',
                'sv': u'Hjälp',
                'ta': u'உதவி',
                'te': u'సహాయము',
                'tg': u'Роҳнамо',
                'th': u'วิธีใช้',
                'tr': u'Yardım',
                'tt': u'Yärdäm',
                #'ty': u'Aide',
                'udm': u'Валэктон',
                'uk': u'Довідка',
                'ur': u'معاونت',
                'vec':u'Aiuto',
                'vi': u'Trợ giúp',
                'wa': u'Aidance',
                'xal': u'Цəəлһлһн',
                'yi': u'הילף',
            },
            13: {
                '_default': u'Help talk',
                'ab': u'Обсуждение справки',
                'af': u'Hulpbespreking',
                'als': u'Hilfe Diskussion',
                'an': u'Descusión aduya',
                'ar': u'نقاش المساعدة',
                'ast': u'Ayuda discusión',
                'av': u'Обсуждение справки',
                'ay': u'Discussion Aide',
                'az': u'Kömək müzakirəsi',
                'ba': u'Белешмә б-са фекер алышыу',
                'bat-smg':u'Pagalbos aptarimas',
                'be': u'Абмеркаваньне дапамогі',
                'bg': u'Помощ беседа',
                'bm': u'Discussion Aide',
                'br': u'Kaozeadenn Skoazell',
                'bs': u'Razgovor o pomoći',
                'ca': u'Ajuda Discussió',
                'ce': u'Обсуждение справки',
                'cs': u'Nápověda diskuse',
                'csb': u'Diskùsëjô Pòmòcë',
                'cv': u'Пулăшăва сӳтсе явмалли',
                'cy': u'Sgwrs Cymorth',
                'da': u'Hjælp diskussion',
                'de': u'Hilfe Diskussion',
                'el': u'Συζήτηση βοήθειας',
                'eo': u'Helpa diskuto',
                'es': u'Ayuda Discusión',
                'et': u'Juhendi arutelu',
                'fa': u'بحث راهنما',
                'fi': u'Keskustelu ohjeesta',
                'fo': u'Hjálp kjak',
                'fr': u'Discussion Aide',
                'fur': u'Discussion jutori',
                'fy': u'Hulp oerlis',
                'ga': u'Plé cabhrach',
                'gn': u'Ayuda Discusión',
                'he': u'שיחת עזרה',
                'hr': u'Razgovor o pomoći',
                'hu': u'Segítség vita',
                'ia': u'Discussion Adjuta',
                'id': u'Pembicaraan Bantuan',
                'is': u'Hjálparspjall',
                'it': u'Discussioni aiuto',
                'ja': u'Help‐ノート',
                'jv': u'Dhiskusi Pitulung',
                'ka': u'დახმარება განხილვა',
                'kn': u'ಸಹಾಯ ಚರ್ಚೆ',
                'ko': u'도움말토론',
                'ku': u'Alîkarî nîqaş',
                'kv': u'Обсуждение справки',
                'la': u'Disputatio Auxilii',
                'li': u'Euverlik help',
                'lt': u'Pagalbos aptarimas',
                'lv': u'Palīdzības diskusija',
                'mk': u'Разговор за помош',
                'ms': u'Perbualan Bantuan',
                'nah': u'Ayuda Discusión',
                'nap': u'Discussioni aiuto',
                'nds': u'Hülp Diskuschoon',
                'nds-nl': u'Overleg help',
                'nl': u'Overleg help',
                'nn': u'Hjelpdiskusjon',
                'no': u'Hjelpdiskusjon',
                'nv': u"Aná'álwo' baa yinísht'į́",
                'oc': u'Discutida Ajuda',
                'os': u'Æххуысы тыххæй дискусси',
                'pa': u'ਮਦਦ ਚਰਚਾ',
                'pl': u'Dyskusja pomocy',
                'pms':u"Discussion ant sl'agiut",
                'pt': u'Ajuda Discussão',
                'qu': u'Ayuda Discusión',
                'rmy':[u'Zhutipen vakyarimata', u'Discuţie Ajutor'],
                'ro': u'Discuţie Ajutor',
                'ru': u'Обсуждение справки',
                'sk': u'Diskusia k pomoci',
                'sl': u'Pogovor o pomoči',
                'sq': u'Ndihmë diskutim',
                'sr': u'Разговор о помоћи',
                'su': u'Obrolan pitulung',
                'sv': u'Hjälpdiskussion',
                'ta': u'உதவி பேச்சு',
                'te': u'సహాయము చర్చ',
                'tg': u'Баҳси роҳнамо',
                'th': u'คุยเรื่องวิธีใช้',
                'tr': u'Yardım tartışma',
                'tt': u'Yärdäm bäxäse',
                #'ty': u'Discussion Aide',
                'udm': u'Валэктон сярысь вераськон',
                'uk': u'Обговорення довідки',
                'ur': u'تبادلۂ خیال معاونت',
                'vec':u'Discussion aiuto',
                'vi': u'Thảo luận Trợ giúp',
                'wa': u'Aidance copene',
                'xal': u'Цəəлһлһин тускар ухалвр',
                'yi': u'הילף רעדן',
            },
            14: {
                '_default': u'Category',
                'ab': u'Категория',
                'af': u'Kategorie',
                'als': u'Kategorie',
                'an': u'Categoría',
                'ar': u'تصنيف',
                'ast': u'Categoría',
                'av': u'Категория',
                'ay': u'Catégorie',
                'az': u'Kateqoriya',
                'ba': u'Категория',
                'bat-smg':u'Kategorija',
                'be': u'Катэгорыя',
                'bg': u'Категория',
                'bm': u'Catégorie',
                'br': u'Rummad',
                'bs': u'Kategorija',
                'ca': u'Categoria',
                'ce': u'Категория',
                'cs': u'Kategorie',
                'csb': u'Kategòrëjô',
                'cv': u'Категори',
                'cy': u'Categori',
                'da': u'Kategori',
                'de': u'Kategorie',
                'el': u'Κατηγορία',
                'eo': u'Kategorio',
                'es': u'Categoría',
                'et': u'Kategooria',
                'eu': u'Kategoria',
                'fa': u'رده',
                'fi': u'Luokka',
                'fo': u'Bólkur',
                'fr': u'Catégorie',
                'fur': u'Categorie',
                'fy': u'Kategory',
                'ga': [u'Catagóir', u'Rang'],
                'gn': u'Categoría',
                'he': u'קטגוריה',
                'hi': u'श्रेणी',
                'hr': u'Kategorija',
                'hu': u'Kategória',
                'ia': u'Categoria',
                'id': u'Kategori',
                'is': u'Flokkur',
                'it': u'Categoria',
                'jv': u'Kategori',
                'ka': u'კატეგორია',
                'kn': u'ವರ್ಗ',
                'ko': u'분류',
                'ku': u'Kategorî',
                'kv': u'Категория',
                'la': u'Categoria',
                'li': u'Kategorie',
                'lt': u'Kategorija',
                'lv': u'Kategorija',
                'mk': u'Категорија',
                'ms': u'Kategori',
                'nah': u'Categoría',
                'nap': u'Categoria',
                'nds': u'Kategorie',
                'nds-nl': u'Categorie',
                'nl': u'Categorie',
                'nn': u'Kategori',
                'no': u'Kategori',
                'nv': u"T'ááłáhági át'éego",
                'oc': u'Categoria',
                'os': u'Категори',
                'pa': u'ਸ਼੍ਰੇਣੀ',
                'pl': u'Kategoria',
                'pms':u'Categorìa',
                'pt': u'Categoria',
                'qu': u'Categoría',
                'rmy':[u'Shopni', u'Categorie'],
                'ro': u'Categorie',
                'ru': u'Категория',
                'sk': u'Kategória',
                'sl': u'Kategorija',
                'sr': u'Категорија',
                'su': u'Kategori',
                'sv': u'Kategori',
                'ta': u'பகுப்பு',
                'te': u'వర్గం',
                'tg': u'Гурӯҳ',
                'th': u'หมวดหมู่',
                'tr': u'Kategori',
                'tt': u'Törkem',
                #'ty': u'Catégorie',
                'udm': u'Категория',
                'uk': u'Категорія',
                'ur': u'زمرہ',
                'vec':u'Categoria',
                'vi': u'Thể loại',
                'wa': u'Categoreye',
                'xal': u'Янз',
                'yi': u'קאַטעגאָריע',
            },
            15: {
                '_default': u'Category talk',
                'ab': u'Обсуждение категории',
                'af': u'Kategoriebespreking',
                'als': u'Kategorie Diskussion',
                'an': u'Descusión categoría',
                'ar': u'نقاش التصنيف',
                'ast': u'Categoría discusión',
                'av': u'Обсуждение категории',
                'ay': u'Discussion Catégorie',
                'az': u'Kateqoriya müzakirəsi',
                'ba': u'Категория б-са фекер алышыу',
                'bat-smg':u'Kategorijos aptarimas',
                'be': u'Абмеркаваньне катэгорыі',
                'bg': u'Категория беседа',
                'bm': u'Discussion Catégorie',
                'br': u'Kaozeadenn Rummad',
                'bs': u'Razgovor o kategoriji',
                'ca': u'Categoria Discussió',
                'ce': u'Обсуждение категории',
                'cs': u'Kategorie diskuse',
                'csb': u'Diskùsëjô Kategòrëji',
                'cv': u'Категорине сӳтсе явмалли',
                'cy': u'Sgwrs Categori',
                'da': u'Kategori diskussion',
                'de': u'Kategorie Diskussion',
                'el': u'Συζήτηση κατηγορίας',
                'eo': u'Kategoria diskuto',
                'es': u'Categoría Discusión',
                'et': u'Kategooria arutelu',
                'eu': u'Kategoria eztabaida',
                'fa': u'بحث رده',
                'fi': u'Keskustelu luokasta',
                'fo': u'Bólkur kjak',
                'fr': u'Discussion Catégorie',
                'fur': u'Discussion categorie',
                'fy': u'Kategory oerlis',
                'ga': u'Plé catagóire',
                'gn': u'Categoría Discusión',
                'he': u'שיחת קטגוריה',
                'hi': u'श्रेणी वार्ता',
                'hr': u'Razgovor o kategoriji',
                'hu': u'Kategória vita',
                'ia': u'Discussion Categoria',
                'id': u'Pembicaraan Kategori',
                'is': u'Flokkaspjall',
                'it': u'Discussioni categoria',
                'ja': u'Category‐ノート',
                'jv': u'Dhiskusi Kategori',
                'ka': u'კატეგორია განხილვა',
                'kn': u'ವರ್ಗ ಚರ್ಚೆ',
                'ko': u'분류토론',
                'ku': u'Kategorî nîqaş',
                'kv': u'Обсуждение категории',
                'la': u'Disputatio Categoriae',
                'li': u'Euverlik kategorie',
                'lt': u'Kategorijos aptarimas',
                'lv': u'Kategorijas diskusija',
                'mk': u'Разговор за категорија',
                'ms': u'Perbualan Kategori',
                'nah': u'Categoría Discusión',
                'nap': u'Discussioni categoria',
                'nds': u'Kategorie Diskuschoon',
                'nds-nl': u'Overleg categorie',
                'nl': u'Overleg categorie',
                'nn': u'Kategoridiskusjon',
                'no': u'Kategoridiskusjon',
                'nv': u"T'ááłáhági át'éego baa yinísht'į́",
                'oc': u'Discutida Categoria',
                'os': u'Категорийы тыххæй дискусси',
                'pa': u'ਸ਼੍ਰੇਣੀ ਚਰਚਾ',
                'pl': u'Dyskusja kategorii',
                'pms':u'Discussion ant sla categorìa',
                'pt': u'Categoria Discussão',
                'qu': u'Categoría Discusión',
                'rmy':[u'Shopni vakyarimata', u'Discuţie Categorie'],
                'ro': u'Discuţie Categorie',
                'ru': u'Обсуждение категории',
                'sk': u'Diskusia ku kategórii',
                'sl': u'Pogovor o kategoriji',
                'sr': u'Разговор о категорији',
                'su': u'Obrolan kategori',
                'sv': u'Kategoridiskussion',
                'ta': u'பகுப்பு பேச்சு',
                'te': u'వర్గం చర్చ',
                'tg': u'Баҳси гурӯҳ',
                'th': u'คุยเรื่องหมวดหมู่',
                'tlh': u"Segh ja'chuq",
                'tr': u'Kategori tartışma',
                'tt': u'Törkem bäxäse',
                #'ty': u'Discussion Catégorie',
                'udm': u'Категория сярысь вераськон',
                'uk': u'Обговорення категорії',
                'ur': u'تبادلۂ خیال زمرہ',
                'vec':u'Discussion categoria',
                'vi': u'Thảo luận Thể loại',
                'wa': u'Categoreye copene',
                'xal': u'Янзин тускар ухалвр',
                'yi': u'קאַטעגאָריע רעדן',
            },
        }
        
        # letters that can follow a wikilink and are regarded as part of this link
        # This depends on the linktrail setting in LanguageXx.php and on
        # [[MediaWiki:Linktrail]].
        # See http://meta.wikipedia.org/wiki/Locales_for_the_Wikipedia_Software
        # to find out the setting for your wiki.
        # Note: this is a regular expression.
        self.linktrails = {
           '_default': u'[a-z]*',
           'de': u'[a-zäöüß]*',
           'da': u'[a-zæøå]*',
           'fr': u'[a-zàâçéèêîôû]*',
           'nl': u'[a-zäöüïëéèéàç]*',
           'pt': u'[a-záâàãéêíóôõúüç]*',
           'ru': u'[a-zа-я]*',
        }
        
        # A dictionary where keys are family codes that can be used in
        # inter-family interwiki links. Values are not used yet.
        # Generated from http://tools.wikimedia.de/~daniel/interwiki-en.txt:
        # remove interlanguage links from file, then run
        # f = open('interwiki-en.txt')
        # for line in f.readlines():
        #     s = line[:line.index('\t')]
        #     print (("            '%s':" % s).ljust(20) + ("'%s'," % s))
        self.known_families = {
            'abbenormal':       'abbenormal',
            'aboutccc':         'aboutccc',
            'acadwiki':         'acadwiki',
            'acronym':          'acronym',
            'advogato':         'advogato',
            'airwarfare':       'airwarfare',
            'aiwiki':           'aiwiki',
            'ajaxxab':          'ajaxxab',
            'alife':            'alife',
            'allwiki':          'allwiki',
            'annotation':       'annotation',
            'annotationwiki':   'annotationwiki',
            'archivecompress':  'archivecompress',
            'archivestream':    'archivestream',
            'arxiv':            'arxiv',
            'aspienetwiki':     'aspienetwiki',
            'atmwiki':          'atmwiki',
            'b':                'wikibooks',
            'battlestarwiki':   'battlestarwiki',
            'bemi':             'bemi',
            'benefitswiki':     'benefitswiki',
            'biblewiki':        'biblewiki',
            'bluwiki':          'bluwiki',
            'bmpcn':            'bmpcn',
            'boxrec':           'boxrec',
            'brasilwiki':       'brasilwiki',
            'brazilwiki':       'brazilwiki',
            'brickwiki':        'brickwiki',
            'bridgeswiki':      'bridgeswiki',
            'bryanskpedia':     'bryanskpedia',
            'bswiki':           'bswiki',
            'bugzilla':         'bugzilla',
            'buzztard':         'buzztard',
            'bytesmiths':       'bytesmiths',
            'c2':               'c2',
            'c2find':           'c2find',
            'cache':            'cache',
            'canyonwiki':       'canyonwiki',
            'canwiki':          'canwiki',
            'Ĉej':              'Ĉej',
            'cellwiki':         'cellwiki',
            'changemakers':     'changemakers',
            'chapter':          'chapter',
            'cheatswiki':       'cheatswiki',
            'chej':             'chej',
            'ciscavate':        'ciscavate',
            'cityhall':         'cityhall',
            'ckwiss':           'ckwiss',
            'cliki':            'cliki',
            'cmwiki':           'cmwiki',
            'cndbname':         'cndbname',
            'cndbtitle':        'cndbtitle',
            'codersbase':       'codersbase',
            'colab':            'colab',
            'comixpedia':       'comixpedia',
            'commons':          'commons',
            'communityscheme':  'communityscheme',
            'consciousness':    'consciousness',
            'corpknowpedia':    'corpknowpedia',
            'cpanelwiki':       'cpanelwiki',
            'choralwiki':       'choralwiki',
            'craftedbycarol':   'craftedbycarol',
            'crazyhacks':       'crazyhacks',
            'creationmatters':  'creationmatters',
            'creatureswiki':    'creatureswiki',
            'cxej':             'cxej',
            'dawiki':           'dawiki',
            'dcdatabase':       'dcdatabase',
            'dcma':             'dcma',
            'dejanews':         'dejanews',
            'delicious':        'delicious',
            'demokraatia':      'demokraatia',
            'devmo':            'devmo',
            'dictionary':       'dictionary',
            'dict':             'dict',
            'disinfopedia':     'disinfopedia',
            'diveintoosx':      'diveintoosx',
            'dndwiki':          'dndwiki',
            'docbook':          'docbook',
            'dolphinwiki':      'dolphinwiki',
            'doom_wiki':        'doom_wiki',
            'drae':             'drae',
            'drumcorpswiki':    'drumcorpswiki',
            'dwellerswiki':     'dwellerswiki',
            'dwjwiki':          'dwjwiki',
            'ebwiki':           'ebwiki',
            'eĉei':             'eĉei',
            'echei':            'echei',
            'echolink':         'echolink',
            'ecoreality':       'ecoreality',
            'ecxei':            'ecxei',
            'editcount':        'editcount',
            'efnetceewiki':     'efnetceewiki',
            'efnetcppwiki':     'efnetcppwiki',
            'efnetpythonwiki':  'efnetpythonwiki',
            'efnetxmlwiki':     'efnetxmlwiki',
            'elibre':           'elibre',
            'eljwiki':          'eljwiki',
            'emacswiki':        'emacswiki',
            'encyclopediadramatica':'encyclopediadramatica',
            'energiewiki':      'energiewiki',
            'eokulturcentro':   'eokulturcentro',
            'evowiki':          'evowiki',
            'fanimutationwiki': 'fanimutationwiki',
            'finalempire':      'finalempire',
            'finalfantasy':     'finalfantasy',
            'finnix':           'finnix',
            'firstwiki':        'firstwiki',
            'flickruser':       'flickruser',
            'floralwiki':       'floralwiki',
            'foldoc':           'foldoc',
            'forthfreak':       'forthfreak',
            'foundation':       'foundation',
            'foxwiki':          'foxwiki',
            'freebio':          'freebio',
            'freebsdman':       'freebsdman',
            'freeculturewiki':  'freeculturewiki',
            'freefeel':         'freefeel',
            'freekiwiki':       'freekiwiki',
            'gamewiki':         'gamewiki',
            'ganfyd':           'ganfyd',
            'gatorpedia':       'gatorpedia',
            'gausswiki':        'gausswiki',
            'gentoo-wiki':      'gentoo-wiki',
            'genwiki':          'genwiki',
            'glencookwiki':     'glencookwiki',
            'globalvoices':     'globalvoices',
            'glossarwiki':      'glossarwiki',
            'glossarywiki':     'glossarywiki',
            'golem':            'golem',
            'google':           'google',
            'googlegroups':     'googlegroups',
            'gotamac':          'gotamac',
            'greencheese':      'greencheese',
            'guildwiki':        'guildwiki',
            'h2wiki':           'h2wiki',
            'hammondwiki':      'hammondwiki',
            'haribeau':         'haribeau',
            'herzkinderwiki':   'herzkinderwiki',
            'hewikisource':     'hewikisource',
            'hkmule':           'hkmule',
            'holshamtraders':   'holshamtraders',
            'hrwiki':           'hrwiki',
            'hrfwiki':          'hrfwiki',
            'humancell':        'humancell',
            'hupwiki':          'hupwiki',
            'iawiki':           'iawiki',
            'imdbname':         'imdbname',
            'imdbtitle':        'imdbtitle',
            'infoanarchy':      'infoanarchy',
            'infobase':         'infobase',
            'infosecpedia':     'infosecpedia',
            'iso639-3':         'iso639-3',
            'iuridictum':       'iuridictum',
            'jameshoward':      'jameshoward',
            'jargonfile':       'jargonfile',
            'javanet':          'javanet',
            'javapedia':        'javapedia',
            'jefo':             'jefo',
            'jiniwiki':         'jiniwiki',
            'jspwiki':          'jspwiki',
            'jstor':            'jstor',
            'kamelo':           'kamelo',
            'karlsruhe':        'karlsruhe',
            'kerimwiki':        'kerimwiki',
            'kinowiki':         'kinowiki',
            'kmwiki':           'kmwiki',
            'knowhow':          'knowhow',
            'kontuwiki':        'kontuwiki',
            'koslarwiki':       'koslarwiki',
            'lanifexwiki':      'lanifexwiki',
            'linuxwiki':        'linuxwiki',
            'linuxwikide':      'linuxwikide',
            'liswiki':          'liswiki',
            'lojban':           'lojban',
            'lollerpedia':      'lollerpedia',
            'lovebox':          'lovebox',
            'lqwiki':           'lqwiki',
            'lugkr':            'lugkr',
            'lurkwiki':         'lurkwiki',
            'lutherwiki':       'lutherwiki',
            'lvwiki':           'lvwiki',
            'm':                'meta',
            'm-w':              'm-w',
            'mail':             'mail',
            'marveldatabase':   'marveldatabase',
            'mathsongswiki':    'mathsongswiki',
            'mbtest':           'mbtest',
            'meatball':         'meatball',
            'mediazilla':       'mediazilla',
            'memoryalpha':      'memoryalpha',
            'meta':             'meta',
            'metareciclagem':   'metareciclagem',
            'metaweb':          'metaweb',
            'metawiki':         'metawiki',
            'metawikipedia':    'metawikipedia',
            'mineralienatlas':  'mineralienatlas',
            'mjoo':             'mjoo',
            'moinmoin':         'moinmoin',
            'mozcom':           'mozcom',
            'mozillawiki':      'mozillawiki',
            'mozillazinekb':    'mozillazinekb',
            'mozwiki':          'mozwiki',
            'musicbrainz':      'musicbrainz',
            'muweb':            'muweb',
            'mw':               'mw',
            'mwod':             'mwod',
            'mwot':             'mwot',
            'myspace':          'myspace',
            'mytips':           'mytips',
            'n':                'wikinews',
            'netvillage':       'netvillage',
            'nkcells':          'nkcells',
            'nomad':            'nomad',
            'nosmoke':          'nosmoke',
            'nost':             'nost',
            'nswiki':           'nswiki',
            'oeis':             'oeis',
            'oldwikisource':    'oldwikisource',
            'onelook':          'onelook',
            'ourpeachtreecorners':'ourpeachtreecorners',
            'openfacts':        'openfacts',
            'opensourcesportsdirectory':'opensourcesportsdirectory',
            'openwetware':      'openwetware',
            'openwiki':         'openwiki',
            'opera7wiki':       'opera7wiki',
            'organicdesign':    'organicdesign',
            'orgpatterns':      'orgpatterns',
            'orthodoxwiki':     'orthodoxwiki',
            'osi reference model':'osi reference model',
            'ourmedia':         'ourmedia',
            'paganwiki':        'paganwiki',
            'panawiki':         'panawiki',
            'pangalacticorg':   'pangalacticorg',
            'patwiki':          'patwiki',
            'perlconfwiki':     'perlconfwiki',
            'perlnet':          'perlnet',
            'personaltelco':    'personaltelco',
            'phwiki':           'phwiki',
            'phpwiki':          'phpwiki',
            'pikie':            'pikie',
            'planetmath':       'planetmath',
            'pmeg':             'pmeg',
            'pmwiki':           'pmwiki',
            'purlnet':          'purlnet',
            'pythoninfo':       'pythoninfo',
            'pythonwiki':       'pythonwiki',
            'pywiki':           'pywiki',
            'psycle':           'psycle',
            'q':                'wikiquote',
            'quakewiki':        'quakewiki',
            'qwiki':            'qwiki',
            'r3000':            'r3000',
            'rakwiki':          'rakwiki',
            'raec':             'raec',
            'redwiki':          'redwiki',
            'revo':             'revo',
            'rfc':              'rfc',
            'rheinneckar':      'rheinneckar',
            'robowiki':         'robowiki',
            'rowiki':           'rowiki',
            'rtfm':             'rtfm',
            's':                'wikisource',
            's23wiki':          's23wiki',
            'scoutpedia':       'scoutpedia',
            'seapig':           'seapig',
            'seattlewiki':      'seattlewiki',
            'seattlewireless':  'seattlewireless',
            'seeds':            'seeds',
            'senseislibrary':   'senseislibrary',
            'sep11':            'sep11',
            'shakti':           'shakti',
            'shownotes':        'shownotes',
            'siliconvalley':    'siliconvalley',
            'slashdot':         'slashdot',
            'slskrex':          'slskrex',
            'smikipedia':       'smikipedia',
            'sockwiki':         'sockwiki',
            'sourceforge':      'sourceforge',
            'sourcextreme':     'sourcextreme',
            'squeak':           'squeak',
            'stockphotoss':     'stockphotoss',
            'strikiwiki':       'strikiwiki',
            'susning':          'susning',
            'svgwiki':          'svgwiki',
            'swinbrain':        'swinbrain',
            'swingwiki':        'swingwiki',
            'tabwiki':          'tabwiki',
            'takipedia':        'takipedia',
            'tamriel':          'tamriel',
            'tavi':             'tavi',
            'tclerswiki':       'tclerswiki',
            'technorati':       'technorati',
            'tejo':             'tejo',
            'terrorwiki':       'terrorwiki',
            'tesoltaiwan':      'tesoltaiwan',
            'thelemapedia':     'thelemapedia',
            'theo':             'theo',
            'theopedia':        'theopedia',
            'theowiki':         'theowiki',
            'theppn':           'theppn',
            'thinkwiki':        'thinkwiki',
            'tibiawiki':        'tibiawiki',
            'tmbw':             'tmbw',
            'tmnet':            'tmnet',
            'tmwiki':           'tmwiki',
            'toyah':            'toyah',
            'trash!italia':     'trash!italia',
            'turismo':          'turismo',
            'tviv':             'tviv',
            'twiki':            'twiki',
            'twistedwiki':      'twistedwiki',
            'tyvawiki':         'tyvawiki',
            'uncyclopedia':     'uncyclopedia',
            'underverse':       'underverse',
            'unreal':           'unreal',
            'ursine':           'ursine',
            'usej':             'usej',
            'usemod':           'usemod',
            'videoville':       'videoville',
            'villagearts':      'villagearts',
            'visualworks':      'visualworks',
            'vkol':             'vkol',
            'voipinfo':         'voipinfo',
            'w':                'wikipedia',
            'warpedview':       'warpedview',
            'webdevwikinl':     'webdevwikinl',
            'webisodes':        'webisodes',
            'webseitzwiki':     'webseitzwiki',
            'wiki':             'wiki',
            'wikia':            'wikia',
            'wikianso':         'wikianso',
            'wikibooks':        'wikibooks',
            'wikichristian':    'wikichristian',
            'wikicities':       'wikicities',
            'wikif1':           'wikif1',
            'wikifur':          'wikifur',
            'wikikto':          'wikikto',
            'wikimac-de':       'wikimac-de',
            'wikimac-fr':       'wikimac-fr',
            'wikimedia':        'wikimedia',
            'wikinews':         'wikinews',
            'wikinfo':          'wikinfo',
            'wikinurse':        'wikinurse',
            'wikipaltz':        'wikipaltz',
            'wikipedia':        'wikipedia',
            'wikipediawikipedia':'wikipediawikipedia',
            'wikiquote':        'wikiquote',
            'wikireason':       'wikireason',
            'wikisophia':       'wikisophia',
            'wikisource':       'wikisource',
            'wikiscripts':      'wikiscripts',
            'wikispecies':      'wikispecies',
            'wikiti':           'wikiti',
            'wikitravel':       'wikitravel',
            'wikitree':         'wikitree',
            'wikiveg':          'wikiveg',
            'wikiwikiweb':      'wikiwikiweb',
            'wikiworld':        'wikiworld',
            'wikt':             'wiktionary',
            'wiktionary':       'wiktionary',
            'wipipedia':        'wipipedia',
            'wlug':             'wlug',
            'wlwiki':           'wlwiki',
            'wmania':           'wmania',
            'wookieepedia':     'wookieepedia',
            'world66':          'world66',
            'wowwiki':          'wowwiki',
            'wqy':              'wqy',
            'wurmpedia':        'wurmpedia',
            'wznan':            'wznan',
            'xboxic':           'xboxic',
            'ypsieyeball':      'ypsieyeball',
            'zrhwiki':          'zrhwiki',
            'zum':              'zum',
            'zwiki':            'zwiki',
            'zzz wiki':         'zzz wiki',
        }
        
        # A list of disambiguation template names in different languages
        self.disambiguationTemplates = {
            '_default': []
        }

        # A list with the name of the category containing disambiguation
        # pages for the various languages. Only one category per language,
        # and without the namespace, so add things like:
        # 'en': "Disambiguation"
        self.disambcatname = {}

        # On most wikis page names must start with a capital letter, but some
        # languages don't use this.
    
        self.nocapitalize = []
    
        # attop is a list of languages that prefer to have the interwiki
        # links at the top of the page.
        self.interwiki_attop = []
        # on_one_line is a list of languages that want the interwiki links
        # one-after-another on a single line
        self.interwiki_on_one_line = []
        
        # String used as separator between interwiki links and the text
        self.interwiki_text_separator = '\r\n\r\n'
        
        # Similar for category
        self.category_attop = []
        # on_one_line is a list of languages that want the category links
        # one-after-another on a single line
        self.category_on_one_line = []
        
        # String used as separator between category links and the text
        self.category_text_separator = '\r\n\r\n'
        
        # When both at the bottom should categories come after interwikilinks?
        self.categories_last = []

        # Which languages have a special order for putting interlanguage links,
        # and what order is it? If a language is not in interwiki_putfirst,
        # alphabetical order on language code is used. For languages that are in
        # interwiki_putfirst, interwiki_putfirst is checked first, and
        # languages are put in the order given there. All other languages are put
        # after those, in code-alphabetical order.
    
        self.interwiki_putfirst = {}

        # Languages in interwiki_putfirst_doubled should have a number plus a list
        # of languages. If there are at least the number of interwiki links, all
        # languages in the list should be placed at the front as well as in the
        # normal list.

        self.interwiki_putfirst_doubled = {}

        # Which language codes do no longer exist and by which language code should
        # they be replaced. If for example the language with code xx: now should get
        # code yy:, add {'xx':'yy'} to obsolete.
    
        self.obsolete = {}
        
        # Language codes of the largest wikis. They should be roughly sorted
        # by size.
        
        self.languages_by_size = []

        # languages in Cyrillic
        self.cyrilliclangs = []
        
        # Main page names for all languages
        self.mainpages = {}

    def _addlang(self, code, location, namespaces = {}):
        """Add a new language to the langs and namespaces of the family.
           This is supposed to be called in the constructor of the family."""
        self.langs[code] = location
        
        for num, val in namespaces.items():
            self.namespaces[num][code]=val
    
    def linktrail(self, code, fallback = '_default'):
        if self.linktrails.has_key(code):
            return self.linktrails[code]
        elif fallback:
            return self.linktrails[fallback]
        else:
            raise KeyError('ERROR: linktrail in language %s unknown' % code)  

    def namespace(self, code, ns_number, fallback = '_default'):
        if not self.isDefinedNS(ns_number):
            raise KeyError('ERROR: Unknown namespace %d' % ns_number)  
        elif self.isNsI18N(ns_number, code):
            v = self.namespaces[ns_number][code]
        elif fallback:
            v = self.namespaces[ns_number][fallback]
        else:
            raise KeyError('ERROR: title for namespace %d in language %s unknown' % (ns_number, code))  

        if type(v) == type([]):
            return v[0]
        else:
            return v

    def isDefinedNS(self, ns_number):
        """Return True if the namespace has been defined in this family.
        """
        return self.namespaces.has_key(ns_number)

    def isNsI18N(self, ns_number, code):
        """Return True if the namespace has been internationalized.
        (it has a custom entry for a given language)"""
        return self.namespaces[ns_number].has_key(code)

    def normalizeNamespace(self, code, value):
        """Given a value, attempt to match it with all available namespaces, with default and localized versions.
        Sites may have more than one way to write the same namespace - choose the first one in the list.
        If nothing can be normalized, return the original value.
        """
        for ns, items in self.namespaces.iteritems():
            if items.has_key(code):
                v = items[code]
                if type(v) == type([]):
                    if value in v: return v[0]
                else:
                    if value == v: return v
            if value == self.namespace('_default', ns):
                return self.namespace(code, ns)
        return value
    
    def disambig(self, code, fallback = '_default'):
        if self.disambiguationTemplates.has_key(code):
            return self.disambiguationTemplates[code]
        elif fallback:
            return self.disambiguationTemplates[fallback]
        else:
            raise KeyError('ERROR: title for disambig template in language %s unknown' % code)  

    # Returns the title of the special namespace in language 'code', taken from
    # dictionary above.
    # If the dictionary doesn't contain a translation, it will use language
    # 'fallback' (or, if fallback isn't given, MediaWiki default).
    # If you want the bot to crash in case of an unknown namespace name, use
    # fallback = None.
    def special_namespace(self, code, fallback = '_default'):
        return self.namespace(code, -1, fallback)
    
    def special_namespace_url(self, code, fallback = '_default'):
        encoded_title = self.namespace(code, -1, fallback).encode(self.code2encoding(code))
        return urllib.quote(encoded_title)
    
    def image_namespace(self, code, fallback = '_default'):
        return self.namespace(code, 6, fallback)
    
    def image_namespace_url(self, code, fallback = '_default'):
        encoded_title = self.namespace(code, 6, fallback).encode(self.code2encoding(code))
        return urllib.quote(encoded_title)
    
    def mediawiki_namespace(self, code, fallback = '_default'):
        return self.namespace(code, 8, fallback)
    
    def template_namespace(self, code, fallback = '_default'):
        return self.namespace(code, 10, fallback)
    
    def category_namespace(self, code, fallback = '_default'):
        return self.namespace(code, 14, fallback)
    
    def category_namespaces(self, code):
        namespaces = []
        namespace_title = self.namespace(code, 14)
        namespaces.append(namespace_title)
        if namespace_title != namespace_title.lower():
            namespaces.append(namespace_title.lower())
        default_namespace_title = self.namespace('_default', 14)
        if namespace_title != default_namespace_title:
            namespaces.append(default_namespace_title)
            if default_namespace_title != default_namespace_title.lower():
                namespaces.append(default_namespace_title.lower())
        return namespaces

    # Redirect code can be translated.

    redirect = {
        'ar': [u'تحويل'],
        'be': [u'перанакіраваньне'],
        'bg': [u'виж'],
        'bs': [u'preusmjeri'],
        'cs': [u'přesměruj'],
        'cy': [u'ail-cyfeirio'],
        'et': [u'suuna'],
        'eu': [u'bidali'],
        'ga': [u'athsheoladh'],
        'he': [u'הפניה'],
        'id': [u'redirected'],
        'is': [u'tilvísun'],
        'nn': [u'omdiriger'],
        'ru': [u'перенаправление', u'перенапр'],
        'sr': [u'преусмери', u'Преусмери'],
        'tt': [u'yünältü']
    }

    # So can be pagename code
    pagename = {
        'bg': [u'СТРАНИЦА'],
        'nn': ['SIDENAMN','SIDENAVN'],
        'ru': [u'НАЗВАНИЕСТРАНИЦЫ'],
        'sr': [u'СТРАНИЦА'],
        'tt': [u'BİTİSEME']
    }

    pagenamee = {
        'nn': ['SIDENAMNE','SIDENAVNE'],
        'ru': [u'НАЗВАНИЕСТРАНИЦЫ2'],
        'sr': [u'СТРАНИЦЕ']
    }

    def pagenamecodes(self,code):
        pos = ['PAGENAME']
        pos2 = []
        if code in self.pagename.keys():
            pos = pos + self.pagename[code]
        elif code == 'als':
            return self.pagenamecodes('de')
        elif code == 'bm':
            return self.pagenamecodes('fr')
        for p in pos:
            pos2 += [p,p.lower()]
        return pos2

    def pagename2codes(self,code):
        pos = ['PAGENAME']
        pos2 = []
        if code in self.pagenamee.keys():
            pos = pos + self.pagenamee[code]
        elif code == 'als':
            return self.pagename2codes('de')
        elif code == 'bm':
            return self.pagename2codes('fr')
        for p in pos:
            pos2 += [p,p.lower()]
        return pos2


        
    # Methods
    
    def hostname(self, code):
        return self.langs[code]
    
    def path(self, code):
        return '/w/index.php'

    def querypath(self, code):
        return '/w/query.php'

    def dbName(self, code):
        # returns the name of the MySQL database
        return '%s%s' % (code, self.name)

    # Which version of MediaWiki is used?

    def version(self, code):
        return "1.5"

    def put_address(self, code, name):
        return '%s?title=%s&action=submit' % (self.path(code), name)

    def get_address(self, code, name):
        return '%s?title=%s&redirect=no' % (self.path(code), name)

    # The URL to get a page, in the format indexed by Google.
    def nice_get_address(self, code, name):
        return '/wiki/%s' % (name)
        
    def edit_address(self, code, name):
        return '%s?title=%s&action=edit' % (self.path(code), name)

    def purge_address(self, code, name):
        return '%s?title=%s&redirect=no&action=purge' % (self.path(code), name)

    def references_address(self, code, name):
        return '%s?title=%s:Whatlinkshere&target=%s&limit=%d' % (self.path(code), self.special_namespace_url(code), name, config.special_page_limit)

    def upload_address(self, code):
        return '%s?title=%s:Upload' % (self.path(code), self.special_namespace_url(code))

    def maintenance_address(self, code, maintenance_page, default_limit = True):
        if default_limit:
            return '%s?title=%s:Maintenance&subfunction=%s' % (self.path(code), self.special_namespace_url(code), maintenance_page)
        else:
            return '%s?title=%s:Maintenance&subfunction=%s&limit=%d' % (self.path(code), self.special_namespace_url(code), maintenance_page, config.special_page_limit)

    def double_redirects_address(self, code, default_limit = True):
        if default_limit:
            return '%s?title=%s:DoubleRedirects' % (self.path(code), self.special_namespace_url(code))
        else:
            return '%s?title=%s:DoubleRedirects&limit=%d' % (self.path(code), self.special_namespace_url(code), config.special_page_limit)

    def broken_redirects_address(self, code, default_limit = True):
        if default_limit:
            return '%s?title=%s:BrokenRedirects' % (self.path(code), self.special_namespace_url(code))
        else:
            return '%s?title=%s:BrokenRedirects&limit=%d' % (self.path(code), self.special_namespace_url(code), config.special_page_limit)

    def allmessages_address(self, code):
        return "%s?title=%s:Allmessages&ot=html" % (self.path(code), self.special_namespace_url(code))

    def login_address(self, code):
        return '%s?title=%s:Userlogin&action=submit' % (self.path(code), self.special_namespace_url(code))

    def watchlist_address(self, code):
        return '%s?title=%s:Watchlist&magic=yes' % (self.path(code), self.special_namespace_url(code))
    
    def move_address(self, code):
        return '%s?title=%s:Movepage&action=submit' % (self.path(code), self.special_namespace_url(code))

    def delete_address(self, code, name):
        return '%s?title=%s&action=delete' % (self.path(code), name)

    def version_history_address(self, code, name):
        return '%s?title=%s&action=history&limit=%d' % (self.path(code), name, config.special_page_limit)

    def export_address(self, code):
        return '%s?title=%s:Export' % (self.path(code), self.special_namespace_url('_default'))

    def query_address(self, code):
        return '%s?' % self.querypath(code)

    def allpages_address(self, code, start, namespace = 0):
        if self.version(code)=="1.2":
            return '%s?title=%s:Allpages&printable=yes&from=%s' % (
                self.path(code), self.special_namespace_url(code), start)
        else:
            return '%s?title=%s:Allpages&from=%s&namespace=%s' % (
                self.path(code), self.special_namespace_url(code), start, namespace)

    def newpages_address(self, code, limit=50):
        return "%s?title=%s:Newpages&limit=%d" % (self.path(code), self.special_namespace_url(code), limit)

    def longpages_address(self, code, limit=500):
        return "%s?title=%s:Longpages&limit=%d" % (self.path(code), self.special_namespace_url(code), limit)

    def shortpages_address(self, code, limit=500):
        return "%s?title=%s:Shortpages&limit=%d" % (self.path(code), self.special_namespace_url(code), limit)

    def categories_address(self, code, limit=500):
        return "%s?title=%s:Categories&limit=%d" % (self.path(code), self.special_namespace_url(code), limit)

    def deadendpages_address(self, code, limit=500):
        return "%s?title=%s:Deadendpages&limit=%d" % (self.path(code), self.special_namespace_url(code), limit)

    def ancientpages_address(self, code, limit=500):
        return "%s?title=%s:Ancientpages&limit=%d" % (self.path(code), self.special_namespace_url(code), limit)

    def lonelypages_address(self, code, limit=500):
        return "%s?title=%s:Lonelypages&limit=%d" % (self.path(code), self.special_namespace_url(code), limit)

    def uncategorizedcategories_address(self, code, limit=500):
        return "%s?title=%s:Uncategorizedcategories&limit=%d" % (self.path(code), self.special_namespace_url(code), limit)
    
    def uncategorizedpages_address(self, code, limit=500):
        return "%s?title=%s:Uncategorizedpages&limit=%d" % (self.path(code), self.special_namespace_url(code), limit)
    
    def unusedcategories_address(self, code, limit=500):
        return "%s?title=%s:Unusedcategories&limit=%d" % (self.path(code), self.special_namespace_url(code), limit)

    def code2encoding(self, code):
        """Return the encoding for a specific language wiki"""
        return 'utf-8'

    def code2encodings(self, code):
        """Return a list of historical encodings for a specific language
           wiki"""
        return self.code2encoding(code),

    def __cmp__(self, otherfamily):
        try:
            return cmp(self.name, otherfamily.name)
        except AttributeError:
            return cmp(id(self), id(otherfamily))

    def RversionTab(self, code):
        """Change this to some regular expression that shows the page we
        found is an existing page, in case the normal regexp does not work."""
        return None

    def getCanonicalIndex(self, namespace):
        """Given a potential namespace, match it with _default values and return namespace index.
        Returns None if not found
        """
        return self.getNsIndex('_default', namespace)

    def getNsIndex(self, lang, namespace):
        """Given a namespace, attempt to match it with all available namespaces.
        Sites may have more than one way to write the same namespace - choose the first one in the list.
        Returns namespace index or None
        """
        namespace = namespace.lower()
        for n in self.namespaces.keys():
            try:
                nslist = self.namespaces[n][lang]
                if type(nslist) != type([]):
                    nslist = [nslist]
                for ns in nslist:
                    if ns.lower() == namespace:
                        return n
            except (KeyError,AttributeError):
                # The namespace has no localized name defined
                pass
        return None
