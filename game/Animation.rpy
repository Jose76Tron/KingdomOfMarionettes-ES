default current_cam = 1

screen cctv_screen():

    add "bg_komputer"

    # Tampilan kamera
    if current_cam == 1:
        add "cctv_cam1" xpos 420 ypos 210
    else:
        add "cctv_cam2" xpos 420 ypos 210

    # KLIK LAYAR → AMATI
    hotspot (420, 210, 500, 280) action Jump("inspect_cctv")

    # INPUT KEYBOARD
    key "K_LEFT" action SetVariable("current_cam", 1)
    key "K_RIGHT" action SetVariable("current_cam", 2)

screen dark_effect():
    add "dark"

screen tangan():
    add "lie_hand"

screen sepatu():
    add "lie_shoe"

screen knibook():
    add "convo_knibook"

screen knihand():
    add "convo_knihand"

screen komputer():
    add "bg_komputer"

screen knipoke():
    add "convo_knipoke"

transform credits_scroll:
    xalign 0.5
    yoffset 900
    linear 30.0 yoffset -2500

transform quick_zoom:
    zoom 1.0
    ease 0.4 zoom 1.4

transform camera_shake:
    xoffset 0 yoffset 0
    linear 0.04 xoffset -15
    linear 0.04 xoffset 15
    linear 0.04 xoffset -10
    linear 0.04 xoffset 10
    linear 0.04 xoffset 0


transform slide_right:
    zoom 1.1
    xalign 0.0
    linear 0.8 xalign 1.0

transform center_pos:
    xalign 0.5

transform right_pos:
    xalign 0.9

transform center_to_right:
    xalign 0.5
    linear 0.5 xalign 0.9

transform quick_turn_left:
    linear 0.18 xpos -350

define config.layers = [ 
    "fill",
    "master",
    "transient",
    "screens",
    "overlay"
]
image bg_fill = Solid("#000000")

#cctv
image cctv main = "cctv_main"
image cctv gate = "cctv_gate"
image cctv corridor1 = "cctv_corridor1"
image cctv stage = "cctv_stage"
image cctv stage2 = "cctv_stage2"
image cctv storage = "cctv_storage"
image cctv storage2 = "cctv_storage2"
image cctv storage3 = "cctv_storage3"
image cctv storage4 = "cctv_storage4"
image cctv theaterhall = "cctv_theaterhall"

#Buat ganti ganti sprite
image jes close normal = "jes_close_normal.png" 
image jes close creep = "jes_close_creep.png" 
image jes close creep2 = "jes_close_creep2.png" 
image jes close smug = "jes_close_smug.png"
image jes close annoy = "jes_close_annoy.png"
image jes close soft = "jes_close_soft.png"
image jes close nosmile = "jes_close_nosmile.png"
image jes close suprais = "jes_close_suprais.png"
image jes close flush = "jes_close_flush.png"
image jes close pout = "jes_close_pout.png"
image jes close laugh = "jes_close_laugh.png"
image jes close flirt = "jes_close_flirt.png"

#buat ganti sprite normalnya jester
image jes bow = "jes_close_miring"
image jes happy = "jes_happy"
image jes happy2 = "jes_happy2"
image jes happy3 = "jes_happy3"
image jes normal = "jes_normal"
image jes normal2 = "jes_normal2"
image jes normal2_2 = "jes_normal2_2"
image jes nosmile = "jes_nosmile"
image jes nosmile2 = "jes_nosmile2"
image jes nosmile2_2 = "jes_nosmile2_2"
image jes nosmile2_3 = "jes_nosmile2_3"
image jes talk = "jes_talk"
image jes talk2 = "jes_talk2"
image jes laugh = "jes_laugh"
image jes laugh2 = "jes_laugh2"
image jes suprais = "jes_suprais"
image jes suprais2 = "jes_suprais2"
image jes suprais3 = "jes_suprais3"
image jes annoy = "jes_annoy"
image jes annoy2 = "jes_annoy2"
image jes annoy3 = "jes_annoy3"
image jes freak = "jes_freak"
image jes flush = "jes_flush"
image jes flush1_2 = "jes_flush1_2"
image jes flush2 = "jes_flush2"
image jes magic = "jes2_magic"
image jes magic2 = "jes_magic2"
image jes creep = "jes_creep"
image jes creep2 = "jes_creep2"
image jes bitch = "jes_bitch"
image jes bitch2 = "jes_bitch2"
image jes bitch3 = "jes_bitch3"
image jes unimpress = "jes_unimpress"
image jes unimpress2 = "jes_unimpress2"
image jes unimpress3 = "jes_unimpress3"
image jes tired = "jes_tired"
image jes pout = "jes_pout"
image jes pout2 = "jes_pout2"
image jes pout3 = "jes_pout3"
image jes nervous2 = "jes_nervous2"
image jes conflic = "jes_conflicted"
image jes glance = "jes_glance"
image jes glance2 = "jes_glance2"
image jes scared = "jes_scared"
image jes breakdown = "jes_breakdown"

#jestyn pas ga make hoodie nya
image jes3 annoy = "jes3_annoy" 
image jes3 furious = "jes3_furious"
image jes3 sad = "jes3_sad"
image jes3 sadsuprais = "jes3_sadsuprais"

#sprite butley hadap depan
image but normal = "butley_normal"
image but suprais = "butley_suprais"
image but smile = "butley_smile"
image but happy = "butley_happy"
image but confuse = "butley_confuse"
image but annoy = "butley_annoy"
image but angry = "butley_angry"
#cg butley
image butcg drag = "butcg_drag"
image butcg pinning = "butcg_pinning"


#jestyn jadi kursi sama disumbat mulutnya
image jescg chair = "jes_chair"
image jescg chair2 = "jes_chair2"
image jescg chair3 = "jes_chair3"
image jescg chair4 = "jes_chair4"
image jescg chair5 = "jes_chair5"
image jescg chair6 = "jes_chair6"
image jescg chair7 = "jes_chair7"
image jescg chair8 = "jes_chair8"
image jescg gagcrief = "jes_gagcrief"
image jescg gagcrief2 = "jes_gagcrief2"
image jescg gagcrief3 = "jes_gagcrief3"
image jescg dinner = "jes_dinner"
image jescg dinner2 = "jes_dinner2"
image jescg dinner3 = "jes_dinner3"
image jescg dinner4 = "jes_dinner4"
image jescg hand = "jescg_hand"
image jescg dinner = "jes_dinner"
image jescg kisshand = "jescg_kisshand"
image jescg kisshand2 = "jescg_kisshand2"
image jescg gagbread = "jes_gagbread"
image jescg gagbread2 = "jes_gagbread2"
image jescg gagbread3 = "jes_gagbread3"
image jescg gagbread4 = "jes_gagbread4"
image jescg gagbread5 = "jes_gagbread5"
image jescg slap = "jescg_slap"
image jescg slap2 = "jescg_slap2"
image jescg slap2_2 = "jescg_slap2_2"
image jescg slap3 = "jescg_slap3"
image jescg slap4 = "jescg_slap4"
image jescg slap5 = "jescg_slap5"
image jescg slap6 = "jescg_slap6"
image jescg slap7 = "jescg_slap7"
image jescg slap8 = "jescg_slap8"
image jescg slap9 = "jescg_slap9"
image jescg slap10 = "jescg_slap10"
image jescg slap11 = "jescg_slap11"
image jescg slap12 = "jescg_slap12"
image jescg slap13 = "jescg_slap13"
image jescg spank = "jescg_spank"
image jescg spank2 = "jescg_spank2"
image jescg spank3 = "jescg_spank3"
image jescg spank4 = "jescg_spank4"
image jescg spank5 = "jescg_spank5"
image jescg spank6 = "jescg_spank6"
image jescg spank7 = "jescg_spank7"
image jescg spank8 = "jescg_spank8"
image jescg spank9 = "jescg_spank9"
image jescg spank10 = "jescg_spank10"
image jescg spank11 = "jescg_spank11"
image jescg spank12 = "jescg_spank12"
image jescg lick = "jescg_lick"
image jescg lick2 = "jescg_lick2"
image jescg lick3 = "jescg_lick3"
image jescg lick4 = "jescg_lick4"
image jescg lick5 = "jescg_lick5"
image jescg lick6 = "jescg_lick6"
image jescg meat = "jescg_meat"
image jescg sleep = "jescg_sleep"
image jescg sleep2 = "jescg_sleep2"
image jescg sleep3 = "jescg_sleep3"
image jescg sleep4 = "jescg_sleep4"
image jescg puppy = "jescg_puppy"
image jescg puppy2 = "jescg_puppy2"
image jescg anxiety = "jescg_anxiety"
image jescg anxiety2 = "jescg_anxiety2"
image jescg anxiety3 = "jescg_anxiety3"
image jescg anxiety4 = "jescg_anxiety4"
image jescg anxiety5 = "jescg_anxiety5"
image jescg anxiety6 = "jescg_anxiety6"
image jescg anxiety7 = "jescg_anxiety7"
image jescg anxiety8 = "jescg_anxiety8"
image jescg anxiety9 = "jescg_anxiety9"

#semua side ch jestyn. yang ada kotaknya
image jessidecg hug = "jescg_hug"
image jessidecg hug2 = "jescg_hug2"

#jestyn dinner scene
image jes dinner normal = "jescg_dinner_normal"
image jes dinner normal2 = "jescg_dinner_normal2"
image jes dinner nosmile = "jescg_dinner_nosmile"
image jes dinner nosmile2 = "jescg_dinner_nosmile2"
image jes dinner smirk = "jescg_dinner_smirk"
image jes dinner smirk2 = "jescg_dinner_smirk2"
image jes dinner love = "jescg_dinner_love"
image jes dinner love2 = "jescg_dinner_love2"
image jes dinner horny = "jescg_dinner_horny"
image jes dinner horny2 = "jescg_dinner_horny2"
image jes dinner mad = "jescg_dinner_mad"
image jes dinner mad2 = "jescg_dinner_mad2"
image jes dinner nosmiletalk = "jescg_dinner_nosmiletalk"
image jes dinner nosmiletalk2 = "jescg_dinner_nosmiletalk2"
image jes dinner suprais = "jescg_dinner_suprais"
image jes dinner suprais2 = "jescg_dinner_suprais2"
image jes dinner smug = "jescg_dinner_smug"
image jes dinner smug2 = "jescg_dinner_smug2"
image jes dinner pout = "jescg_dinner_pout"
image jes dinner pout2 = "jescg_dinner_pout2"
image jes dinner sad = "jescg_dinner_sad"
image jes dinner sad2 = "jescg_dinner_sad2"
image jes dinner giggle = "jescg_dinner_giggle"
image jes dinner giggle2 = "jescg_dinner_giggle2"
image jes dinner giggle3 = "jescg_dinner_giggle3"

#buat ganti sprite normalnya wizzy
image wiz normal = "wiz_normal"
image wiz normal1_2 = "wiz_normal1_2"
image wiz normal2 = "wiz_normal2"
image wiz normal2_2 = "wiz_normal2_2"
image wiz talk = "wiz_talk"
image wiz talk1_2 = "wiz_talk1_2"
image wiz talk2 = "wiz_talk2"
image wiz talk2_2 = "wiz_talk1_2"
image wiz nosmile = "wiz_nosmile"
image wiz nosmile1_2 = "wiz_nosmile1_2"
image wiz nosmile2 = "wiz_nosmile2"
image wiz nosmile2_2 = "wiz_nosmile2_2"
image wiz nervous = "wiz_nervous"
image wiz nervous1_2 = "wiz_nervous1_2"
image wiz nervous2 = "wiz_nervous2"
image wiz nervous2_2 = "wiz_nervous2_2"
image wiz panic = "wiz_panic"
image wiz panic1_2 = "wiz_panic1_2"
image wiz panic2 = "wiz_panic2"
image wiz panic2_2 = "wiz_panic2_2"
image wiz pout = "wiz_pout"
image wiz pout1_2 = "wiz_pout1_2"
image wiz pout2 = "wiz_pout2"
image wiz pout2_2 = "wiz_pout2_2"
image wiz sad = "wiz_sad"
image wiz sad1_2 = "wiz_sad1_2"
image wiz sad2 = "wiz_sad2"
image wiz sad2_2 = "wiz_sad2_2"
image wiz angry = "wiz_angry"
image wiz angry1_2 = "wiz_angry1_2"
image wiz angry2 = "wiz_angry2"
image wiz angry2_2 = "wiz_angry2_2"
image wiz smirk1_2 = "wiz_smirk1_2"
image wiz smirk2_2 = "wiz_smirk2_2"

# buat cg wizzy pas lagi ngobrol
image wizconvo normal = "wizconvo_normal"
image wizconvo normal2 = "wizconvo_normal2"
image wizconvo normal3 = "wizconvo_normal3"
image wizconvo nosmile = "wizconvo_nosmile"
image wizconvo nosmile2 = "wizconvo_nosmile2"
image wizconvo nosmile3 = "wizconvo_nosmile3"
image wizconvo happy = "wizconvo_happy"
image wizconvo happy2 = "wizconvo_happy2"
image wizconvo happy3 = "wizconvo_happy3"
image wizconvo talk = "wizconvo_talk"
image wizconvo talk2 = "wizconvo_talk2"
image wizconvo talk3 = "wizconvo_talk3"
image wizconvo nervous = "wizconvo_nervous"
image wizconvo nervous2 = "wizconvo_nervous2"
image wizconvo nervous3 = "wizconvo_nervous3"
image wizconvo smirk = "wizconvo_smirk"
image wizconvo smirk2 = "wizconvo_smirk2"
image wizconvo smirk3 = "wizconvo_smirk3"
image wizconvo suprais = "wizconvo_suprais"
image wizconvo suprais2 = "wizconvo_suprais2"
image wizconvo suprais3 = "wizconvo_suprais3"
image wizconvo hat = "wizconvo_hat"
image wizconvo hat2 = "wizconvo_hat2"
image wizconvo hat3 = "wizconvo_hat3"
image wizconvo hat4 = "wizconvo_hat4"
image wizconvo hat5 = "wizconvo_hat5"
image wizconvo hat6 = "wizconvo_hat6"
image wizconvo hat7 = "wizconvo_hat7"
image wizconvo hat8 = "wizconvo_hat8"
image wizconvo hat9 = "wizconvo_hat9"
image wizconvo pout = "wizconvo_pout"
image wizconvo pout2 = "wizconvo_pout2"
image wizconvo pout3 = "wizconvo_pout3"
image wizconvo mad = "wizconvo_mad"
image wizconvo mad4 = "wizconvo_mad4"
image wizconvo breakdown = "wizconvo_breakdown"
image wizconvo breakdown2 = "wizconvo_breakdown2"
image wizconvo breakdown3 = "wizconvo_breakdown3"
image wizconvo blush = "wizconvo_blush"

#sprite jestyn yang collar
image jes collar normal = "jes_collar_normal"
image jes collar normal2 = "jes_collar_normal2"
image jes collar talk = "jes_collar_talk"
image jes collar talk2 = "jes_collar_talk2"
image jes collar flush = "jes_collar_flush"
image jes collar flush2 = "jes_collar_flush2"
image jes collar freak = "jes_collar_freak"
image jes collar freak2 = "jes_collar_freak2"
image jescg dielus = "jes_dielus"
image jescg dielus2 = "jes_dielus2"
image jescg dielus3 = "jes_dielus3"
image jescg dielus2_1 = "jes_dielus2_1"
image jescg dielus2_2 = "jes_dielus2_2"
image jescg freaky = "jescg_freaky"
image jescg freaky2 = "jescg_freaky2"
image jescg freaky3 = "jescg_freaky3"
image jescg freaky4 = "jescg_freaky4"
image jescg obsess = "jescg_obses"
image jescg obsess2 = "jescg_obses2"
image jescg obsess3 = "jescg_obses3"
image jescg obsess4 = "jescg_obses4"
image jescg obsess5 = "jescg_obses5"
image jescg obsess6 = "jescg_obses6"
image jescg leftright = "left_or_right"
image jescg snakedoll = "snakedoll"
image jescg bunnydoll = "bunnydoll"
image cg dance = "cg_dance"
image cg dance2 = "cg_dance2"
image cg dance3 = "cg_dance3"
image cg dance4 = "cg_dance4"
image cg dance5 = "cg_dance5"
image cg danceblur = "cg_danceblur"
image cg cursed = "cursed"
image cg cursed2 = "cursed2"
image cg cursed3 = "cursed3"
image jescg bed normal = "jescg_bed_normal"
image jescg bed blush = "jescg_bed_blush"
image jescg bed lookaway = "jescg_bed_lookaway"
image jescg bed nosmile = "jescg_bed_nosmile"
image jescg bed sad = "jescg_bed_sad"
image jescg bed pout = "jescg_bed_pout"
image jescg bed caress = "jescg_bed_caress"
image jescg fairytale = "jescg_fairytale"
image jescg fairytale2 = "jescg_fairytale2"
image jescg fairytale3 = "jescg_fairytale3"
image jescg fairytale4 = "jescg_fairytale4"
image jescg fairytale5 = "jescg_fairytale5"
image jescg fairytale6 = "jescg_fairytale6"
image jescg deerfairytale = "jescg_deerfairytale"
image jescg owlfairytale = "jescg_owlfairytale"
image jescg dogfairytale = "jescg_dogfairytale"
image jescg lionfairytale = "jescg_lionfairytale"
image jescg bunnyfairytale = "jescg_bunnyfairytale"
image jescg bunnyfairytale2 = "jescg_bunnyfairytale2"
image jescg bunnyfairytale3 = "jescg_bunnyfairytale3"
image jescg lionbunfairytale = "jescg_lionbunfairytale"
image jescg lionbunfairytale2 = "jescg_lionbunfairytale2"
image jescg fairytale7 = "jescg_fairytale7"
image jescg fairytale8 = "jescg_fairytale8"

#sprite jestyn yang ke dua
image jes2 normal = "jes2_normal"
image jes2 normal2 = "jes2_normal2"
image jes2 normal3 = "jes2_normal3"
image jes2 smug = "jes2_smug"
image jes2 smug2 = "jes2_smug2"
image jes2 talk = "jes2_talk"
image jes2 talk2 = "jes2_talk2"

#cg sit nya jestyn
image jes crawl normal = "cg_crawl"
image jes crawl talk = "cg_crawl_talk"
image jes crawl smug = "cg_crawl_smug"
image jes crawl flush = "cg_crawl_flush"
image jes crawl mad = "cg_crawl_mad"
image jes lap = "jes_lap"
image jes lap2 = "jes_lap2"
image jes lap3 = "jes_lap3"
image jes lap4 = "jes_lap4"
image jes lie = "jes_lie"
image jes lie2 = "jes_lie2"
image jes lie3 = "jes_lie3"
image jes lie4 = "jes_lie4"
image jes lie5 = "jes_lie5"
image jes lie6 = "jes_lie6"
image jes lie7 = "jes_lie7"
image jesmeat2 = "jes_meat2"

#cg day2 pas jestyn megang bahu mc dari belakang
image jes backday2 = "jescg_backday2"
image jes backday2_2 = "jescg_backday2_2"
image jes backday2_3 = "jescg_backday2_3"

#cg jestyn pas crownus room
image jes crownus room = "cg_jescrowroom"
image jes crownus room2 = "cg_jescrowroom2"
image jes crownus room3 = "cg_jescrowroom3"


#sprite npc farmer
image farm sad = "farm_sad"
image farm happy = "farm_happy"
image farm suprais = "farm_suprais"
image farm sad2 = "farm_sad2"
image farm close = "farm_close"
image farm close6 = "farm_close6"

#pas prieston nyamar jadi jestyn
image jespri normal = "jespri_normal"
image jespri laugh = "jespri_laugh"
image jespri creep = "jespri_creep"
image jespri nosmile = "jespri_nosmile"
image jespri nosmile2 = "jespri_nosmile2"
image jespri smileclose = "jespri_smileclose"
image jespri smirk = "jespri_smirk"
image jespri talk = "jespri_talk"

#cg prieston
image pricg poke = "pricg_poke"
image pricg poke2 = "pricg_poke2"
image pricg poke3 = "pricg_poke3"
image pricg poke4 = "pricg_poke4"
image pricg reveal = "pricg_reveal"
image pricg reveal2 = "pricg_reveal2"
image pricg reveal3 = "pricg_reveal3"
image pricg reveal4 = "pricg_reveal4"
image pricg reveal5 = "pricg_reveal5"
image pricg reveal6 = "pricg_reveal6"
image pricg revealyey = "pricg_revealyey"
image pricg revealyey2 = "pricg_revealyey2"
image pricg revealyey3 = "pricg_revealyey3"
image pricg revealyey4 = "pricg_revealyey4"
image pricg bed smile = "pricg_bed_smile"
image pricg bed smile2 = "pricg_bed_smile2"
image pricg bed smile3 = "pricg_bed_smile3"
image pricg bed smile4 = "pricg_bed_smile4"
image pricg bed smile5 = "pricg_bed_smile5"
image pricg bed nosmile = "pricg_bed_nosmile"
image pricg bed close = "pricg_bed_close"

#sprite prieston
image pri suprais = "pri_suprais"
image pri suprais2 = "pri_suprais2"
image pri sad = "pri_sad"
image pri sad2 = "pri_sad2"
image pri nosmile = "pri_nosmile"
image pri nosmile2 = "pri_nosmile2"
image pri normal = "pri_normal"
image pri normal2 = "pri_normal2"
image pri happy = "pri_happy"
image pri happy2 = "pri_happy2"
image pri gentle = "pri_gentle"
image pri gentle2 = "pri_gentle2"
image pri creep = "pri_creep"
image pri creep2 = "pri_creep2"
image pri annoy = "pri_annoy"
image pri annoy2 = "pri_annoy2"
image pri amused = "pri_amused"
image pri amused2 = "pri_amused2"
image pri talk = "pri_talk"
image pri talk2 = "pri_talk2"

#Prieston pas ngobrol di meja
image pri table amused = "pri_table_amused"
image pri table amused2 = "pri_table_amused2"
image pri table annoy = "pri_table_annoy"
image pri table annoy2 = "pri_table_annoy2"
image pri table creep = "pri_table_creep"
image pri table creep2 = "pri_table_creep2"
image pri table gentle = "pri_table_gentle"
image pri table gentle2 = "pri_table_gentle2"
image pri table laugh = "pri_table_laugh"
image pri table laugh2 = "pri_table_laugh2"
image pri table normal = "pri_table_normal"
image pri table normal2 = "pri_table_normal2"
image pri table nosmile = "pri_table_nosmile"
image pri table nosmile2 = "pri_table_nosmile2"
image pri table talk = "pri_table_talk"
image pri table talk2 = "pri_table_talk2"


#sprite the maids
image maidelyn normal = "maidelyn_normal"
image maidelyn nosmile = "maidelyn_nosmile"
image maidelyn annoy = "maidelyn_annoy"
image maidelyn happy = "maidelyn_happy"
image maidelyn laugh = "maidelyn_laugh"
image maidelyn suprais = "maidelyn_talk"
image maidelyn talk = "maidelyn_talk"

image maidy normal = "maidy_normal"
image maidy polite = "maidy_polite"
image maidy happy = "maidy_happy"
image maidy nosmile = "maidy_nosmile"
image maidy panic = "maidy_panic"
image maidy pout = "maidy_pout"
image maidy normal = "maidy_normal"
image maidy estatic = "maidy_estatic"

image maidra normal = "maidra_normal"
image maidra polite = "maidra_polite"
image maidra smug = "maidra_smug"
image maidra suprais = "maidra_suprais"
image maidra mad = "maidra_mad"
image maidra nosmile = "maidra_nosmile"
image maidra sad = "maidra_sad"
image maidra blush = "maidra_blush"
image maidra estatic = "maidra_estatic"

#sprite knighter
image kni normal = "kni_normal"
image kni normal2 = "kni_normal2"
image kni annoy = "kni_annoy"
image kni annoy2 = "kni_annoy2"
image kni confuse = "kni_confuse"
image kni confuse = "kni_confuse2"
image kni hahh = "kni_hahh"
image kni hahh2 = "kni_hahh2"
image kni hat = "kni_hat"
image kni hat2 = "kni_hat2"
image kni mad = "kni_mad"
image kni mad2 = "kni_mad2"
image kni sad = "kni_sad"
image kni sad2 = "kni_sad2"
image kni suprais = "kni_suprais"
image kni suprais2 = "kni_suprais2"
image kni talk = "kni_talk"
image kni talk2 = "kni_talk2"
image kni talkaway = "kni_talkaway"
image kni talkaway2 = "kni_talkaway2"
image kni glance = "kni_glance"
image kni glance2 = "kni_glance2"
image kni flush = "kni_flush"

# convo knighter
image kni convo annoy = "kni_convo_annoy"
image kni convo blush = "kni_convo_blush"
image kni convo close = "kni_convo_close"
image kni convo flush = "kni_convo_flush"
image kni convo gentle = "kni_convo_gentle"
image kni convo normaldown = "kni_convo_normaldown"
image kni convo normalup = "kni_convo_normalup"
image kni convo sad = "kni_convo_sad"
image kni convo smirk = "kni_convo_smirk"
image kni convo suprais = "kni_convo_suprais"
image kni convo talkdown = "kni_convo_talkdown"
image kni convo talkup = "kni_convo_talkup"
image kni convo disgust = "kni_convo_disgust"
image kni convo jes = "kni_convo_jes"
image kni convo cubit = "kni_convo_cubit"
image kni convo cubit2 = "kni_convo_cubit2"
image kni convo cubit3 = "kni_convo_cubit3"
#tangan knighter pas ngobrol
image convo knihand = "convo_knihand"
image convo knibook = "convo_knibook"

#cg knighter
image knicg fight = "knicg_fight"
image knicg fight2 = "knicg_fight2"
image knicg fight3 = "knicg_fight3"
image knicg fight4 = "knicg_fight4"
image knicg fight5 = "knicg_fight5"

# jestyn sama knighter
image jestynkni = "jeskni_1"
image jestynkni2 = "jeskni_2"
image jestynkni3 = "jeskni_3"
image jestynkni4 = "jeskni_4"
image jestynkni5 = "jeskni_5"

#Animasi tangan jestyn nutupin mata mc
image hand_cover:
    "hand_cover1"
    pause 0.1
    "hand_cover2"
    pause 0.1
    "hand_cover3"
    pause 0.1
    zoom 1.3
    "black_area"
    pause 0.1

image kedip:
    "kedip1"
    pause 0.5
    "kedip2"
    pause 0.5
    "kedip3"
    pause 0.5
    "kedip4"
    pause 0.5
    
image merem:
    "kedip4"
    pause 0.2
    "kedip3"
    pause 0.2
    "kedip2"
    pause 0.2
    "kedip1"
    pause 0.2
    "black_area"
    pause 0.2

image bzzt:
    "bzzt1"
    pause 0.1
    "bzzt2"
    pause 0.1
    "bzzt3"
    pause 0.1
    "bzzt4"
    pause 0.1
    
#animasi mata geter pas mc maksa masuk ke kamar crownus
image matageter:
    "cg_matageter"
    pause 0.1 
    "cg_matageter3"
    pause 0.1
    "cg_matageter4"
    pause 0.1
    "cg_matageter2"
    pause 0.1
    "cg_matageter5"
    pause 0.1
    repeat


image anim fairytale:
    "cg_fairytale"
    pause 0.8 
    "cg_fairytale2"
    pause 0.8
    repeat

image anim feast fairytale:
    "feast_fairytale"
    pause 0.8 
    "feast_fairytale2"
    pause 0.8
    repeat

image anim glitch fairytale:
    "glitch_fairytale"
    pause 0.1
    "glitch_fairytale2"
    pause 0.1
    "glitch_fairytale3"
    pause 0.1
    "glitch_fairytale4"
    pause 0.1
    "jescg_white"
    pause 0.1
    "glitch_fairytale5"
    pause 0.1
    "glitch_fairytale6"
    pause 0.1
    "glitch_fairytale7"
    pause 0.1
    "bg_darkfairytale"
    pause 0.1

image anim lionfall:
    "jescg_white"
    pause 0.1
    "lionfall"
    pause 0.1
    "lionfall2"
    pause 0.1
    "lionfall3"
    pause 0.1
    "lionfall4"
    pause 0.1
    "lionfall6"
    pause 0.1
    "lionfall5"
    pause 0.1
    "lionfall7"
    pause 0.1
    "lionfall8"
    pause 0.1
    "lionfall9"
    pause 0.5
    "lionfall7"
    pause 0.1
    "lionfall8"
    pause 0.1
    "lionfall6"
    pause 0.1
    "lionfall5"
    pause 0.1
    "lionfall4"
    pause 1.0

    
    
   

#aimasi prieston pas di tempat tidur
image anim pri cg bed:
    "pricg_bed_smile"
    pause 0.1 
    "pricg_bed_smile2"
    pause 0.1
    "pricg_bed_smile3"
    pause 0.1
    "pricg_bed_smile5"
    pause 0.1
    "pricg_bed_smile4"
    pause 0.1

#animasi jestyn ngelus tangan mc
image ngelus:
    "tangan1"
    pause 1.0
    "tangan2"
    pause 0.2
    "tangan3"
    pause 0.2
    "tangan4"
    pause 0.2
    "tangan5"
    pause 0.2
    "tangan6"
    pause 1.0
    "tangan5"
    pause 0.2
    "tangan4"
    pause 0.2
    "tangan3"
    pause 0.2
    "tangan2"
    pause 0.2
    repeat

image farm close anim:
    "farm_close1"
    pause 0.2
    "farm_close2"
    pause 0.2
    "farm_close3"
    pause 0.2
    "farm_close4"
    pause 0.2
    "farm_close5"
    pause 0.2
    "farm_close4"
    pause 0.2
    "farm_close3"
    pause 0.2
    "farm_close2"
    pause 0.2
    repeat

#animasi main menu
image newmenu_flicker:

    Null()

    pause 0.07

    Solid("#000000")

    pause 0.03

    Null()

    pause 0.12

    Solid("#000000")

    pause 0.2

    Null()

    pause 5.0

    Solid("#000000")

    pause 1.0

    repeat

image menu_flicker:
    "gui/main_menu.png"
    pause 0.07
    "gui/main_menu2.png"
    pause 0.03
    "gui/main_menu.png"
    pause 0.12
    "gui/main_menu2.png"
    pause 0.2
    "gui/main_menu.png"
    pause 2.0
    "gui/main_menu2.png"
    pause 1.0
    repeat

image wizconvo anim:
    "wizconvo_hat3"
    pause 0.1
    "wizconvo_hat4"
    pause 0.1
    "wizconvo_hat5"
    pause 0.1
    "wizconvo_hat6"
    pause 0.1
    "wizconvo_hat7"
    pause 0.1
    "wizconvo_hat8"
    pause 0.1
    "wizconvo_hat9"
    pause 0.1

image glitch jesslap:
    "jescg_white"
    pause 0.1
    "jescg_glitchslap5"
    pause 0.1
    "jescg_glitchslap2"
    pause 0.1
    "jescg_glitchslap4"
    pause 0.1
    "jescg_glitchslap3"
    pause 0.1
    "jescg_glitchslap"
    pause 0.1
    "jescg_glitchslap4"
    pause 0.1
    "jescg_glitchslap2"
    pause 0.1
    "jescg_glitchslap3"
    pause 0.1
    "jescg_glitchslap5"
    pause 0.1
    "jescg_white"
    pause 0.1
    "jescg_slap6"
    pause 0.1


image glitch2 jesspank:
    "jescg_white"
    pause 0.1
    "jescg_glitchspank"
    pause 0.1
    "jescg_glitchspank3"
    pause 0.1
    "jescg_glitchspank5"
    pause 0.1
    "jescg_glitchspank2"
    pause 0.1
    "jescg_glitchspank4"
    pause 0.1
    "jescg_glitchspank6"
    pause 0.1
    "jescg_glitchspank2"
    pause 0.1
    "jescg_glitchspank5"
    pause 0.1
    "jescg_glitchspank"
    pause 0.1
    "jescg_white"
    pause 0.1
    "jescg_spank7"
    pause 0.1

transform nightmare_text:

    xalign 0.5
    yalign 0.5

    linear 0.03 xoffset -4 yoffset -2
    linear 0.03 xoffset 4 yoffset 3
    linear 0.03 xoffset -3 yoffset 2
    linear 0.03 xoffset 2 yoffset -3
    repeat

screen dream_text(msg):

    frame:
        background None
        xalign 0.5
        yalign 0.5

        text msg:
            size 60
            xalign 0.5
            yalign 0.5
        
