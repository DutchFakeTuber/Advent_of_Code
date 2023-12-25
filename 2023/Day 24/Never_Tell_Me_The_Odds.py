TEST: str = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

DATA: str = """230027994633462, 224850233272831, 164872865225455 @ 103, -57, 285
213762157019377, 204038908928791, 198113097692531 @ 184, -110, 174
236440979253526, 104012423941037, 223798957622735 @ 15, 694, -277
150273374343556, 50901286038655, 131546537769893 @ 272, 413, 324
218468515688398, 199700421155153, 351097822373397 @ 123, 113, -104
338621759011922, 241627500098406, 284905984709165 @ -217, -83, -76
201589965927467, 279704038327366, 196206631637120 @ 190, -213, 185
364600907847245, 443329607619619, 466958764329116 @ -32, -66, -79
235508132991422, 298506086473913, 413412591314453 @ 94, 43, -70
335439655104640, 287678332331229, 259037521410669 @ -123, -92, 52
127080465083842, 91287599329741, 61446566878670 @ 335, 332, 491
184418203088091, 238465435208692, 207167094388365 @ 256, -117, 148
416343629775116, 253022765045891, 491717629266329 @ -92, 115, -118
481449962915902, 299668862140153, 547428270008293 @ -156, 69, -171
353659351929670, 307378415986126, 458883909389384 @ -37, 45, -105
345124099531431, 208340262699411, 232237319323881 @ -184, 50, 96
202300175388116, 12655440829711, 313967152251771 @ 212, 705, -275
316973823196462, 310028917628689, 359270794507349 @ -41, -51, -80
273480679077424, 181142079537670, 196085590194980 @ -147, -47, 183
265521512671375, 151640201406799, 273771107951019 @ -78, 138, -218
271285717225275, 283711136190258, 305929300939687 @ 26, -37, -14
175551166933357, 31306715871346, 277735095312815 @ 176, 379, 74
273666334571593, 422558547907705, 443492149303658 @ 50, -96, -99
229387426042768, 169123293575863, 264612930601025 @ 102, 181, 78
179539247670742, 302106667444141, 142579620797445 @ 213, -135, 304
313951911510967, 251555559461716, 256970350655570 @ -138, -103, 11
406438277711560, 365452366481665, 303153811346747 @ -99, -24, 66
175487869090582, 332758416807097, 262178100537797 @ 159, 24, 116
310857408788602, 297796477288243, 210531244259195 @ -31, -31, 163
290914838024874, 249881426224863, 303478502955052 @ 7, 58, 21
315153759144108, 323822771889631, 317484883061809 @ -19, -30, 16
314531736895682, 304288250087625, 405806411638705 @ 14, 64, -27
359828517222499, 160673816668009, 329170273114796 @ -44, 208, 39
255034684146830, 152507643183922, 117096373014354 @ -29, 129, 609
240328800947362, 177152930485741, 173839173482525 @ 77, 130, 240
273825352380936, 138607753598081, 279984054680611 @ -28, 220, -65
213205983759112, 258423997273651, 351867124633705 @ 129, 30, -72
245195306496019, 481091129117122, 407197424551190 @ 56, -839, -467
154285975864047, 248757027714604, 345592152643047 @ 184, 111, 22
488085922423580, 495215392032367, 260502996061357 @ -200, -183, 112
257029813969903, 37373163859165, 313395965565740 @ 26, 508, -147
230453727878930, 306197584387773, 337303048171909 @ 100, 29, 16
329630073824428, 392403119779285, 320159344551311 @ -12, -54, 47
304859069662267, 346759281854758, 396344664342960 @ 24, 21, -17
283615259850910, 176077346765753, 282824877123573 @ -42, 121, -48
264643697109766, 397536034297309, 330929300678258 @ -5, -588, -235
266011575273610, 360696689080581, 225549285492625 @ 36, -175, 133
276302661941806, 344515870053721, 332797867109285 @ 27, -100, -32
326007133498669, 262754120817097, 259969586987480 @ -40, 48, 93
255959563334032, 388577753395537, 317216656651667 @ 29, -488, -158
239430563125187, 358004224071011, 182824431038620 @ 76, -398, 223
262478724774643, 201828772642917, 229303327495039 @ -42, -76, 34
236662654787686, 343798503126673, 358183162597277 @ 88, -193, -145
272796129537928, 506323927552474, 395890365744344 @ 45, -247, -73
277996237072567, 263751976057756, 314960482794235 @ -36, -141, -158
209060297591344, 397718102372343, 386150519651013 @ 126, -83, -44
224729179946206, 239992006097185, 335246207462327 @ 115, -24, -154
320806761721630, 350129757817168, 190254124594029 @ -45, -111, 196
300383251736227, 314697575293711, 230151124509260 @ 6, -6, 141
298799168709265, 323028208516999, 528028497088307 @ -84, -278, -714
264849550365178, 273365322324321, 240409847851501 @ -60, -430, -26
211062150584181, 52373975127725, 144934489260904 @ 220, 716, 489
295419252680462, 311297839567761, 43898700236365 @ 35, 61, 339
250363519229090, 214880583149241, 316368318115341 @ 53, 40, -104
268132731730239, 90221494545328, 304578508795582 @ 38, 309, 7
254622077432554, 174402670929509, 355332297100035 @ 21, 98, -347
280473885806842, 315439639491991, 204057564976545 @ -57, -342, 160
240136614510064, 452723099922549, 305446649733141 @ 90, -86, 76
237672829959342, 156081505063166, 213208394929895 @ 67, 119, 98
332664810743172, 361669914191796, 404581421906855 @ -55, -109, -130
276074637821906, 414382905781511, 269440279576457 @ -35, -605, -34
290356114063054, 255844093656841, 208034612661749 @ -44, -60, 157
233250296756043, 196219253340810, 188599633119778 @ 88, -119, 225
273573707309188, 252111546835477, 326561726006651 @ 42, 78, 11
366660156271742, 311219459221641, 181779462584645 @ -52, 40, 203
192771897012462, 356765993503501, 179412123771505 @ 155, -87, 211
246089656339000, 189736829986477, 263165370636619 @ 36, -6, -101
331706243127232, 320892065496394, 412514267667047 @ -11, 33, -50
256886052035982, 311151797027721, 311736537912597 @ 59, -40, 6
292283147915314, 285340455714613, 146240267727419 @ 33, 74, 241
316864302124125, 344426610944628, 388514316012692 @ 10, 19, -13
245162026648332, 151686836111271, 221026775396945 @ -14, 79, -22
190653386950192, 318788912048851, 256438229364079 @ 174, -105, 75
334445194831732, 174483874959021, 217334729450900 @ -27, 188, 161
222578364011099, 265728919700523, 166123223520646 @ 128, -206, 285
252356893967347, 237617659393063, 252298277764517 @ 34, -86, 12
219705604665928, 262074818367097, 290169358828841 @ 168, -536, -378
185526123108625, 275704760226523, 232037153688488 @ 232, -178, 81
271835657199025, 225548947956805, 259523803670240 @ -24, -44, -7
334204299629902, 382142978011435, 143122292633819 @ -61, -149, 269
393118185137200, 478470779332545, 362787847275700 @ -99, -184, -17
436755514203224, 187597352235695, 548569354764229 @ -115, 182, -180
388991600755302, 462593804229041, 293924943559869 @ -56, -85, 91
356853667041280, 283811594336566, 369411027786959 @ -87, 15, -70
342671248372318, 427294051575172, 389168408981630 @ -13, -57, -7
370231487147908, 168797500835101, 197687170506209 @ -127, 180, 184
271172863220963, 428673526571846, 344097283281338 @ 58, -65, 35
231160991933494, 148592672884885, 202946893610765 @ 101, -41, 58
146390717413456, 174177503934083, 47807393881401 @ 342, 119, 610
368155904189527, 343784450242426, 274603519024650 @ -120, -99, 61
311380499072307, 243234127877111, 256050114032853 @ -196, -170, -36
219122006445004, 276865327907671, 153143362903475 @ 125, -70, 278
340973826002157, 428823963637441, 383274841117985 @ -34, -120, -40
192019121044078, 167337978702889, 191158148683853 @ 263, 92, 205
234595229431186, 189461041605333, 259072147442841 @ 60, -437, -563
345181024845667, 408915567151033, 510506586160703 @ -26, -64, -158
245468443912894, 311039963189335, 245479484380975 @ 75, -63, 103
324305577941707, 477432175015111, 118149301599794 @ -6, -150, 275
248839083976474, 149139803047537, 226202082738053 @ -62, 82, -96
305025253783262, 343004172818502, 349171594144548 @ 19, 11, 21
219678828088606, 222017117365609, 166270516467797 @ 228, -762, 510
347055419549452, 241067578498099, 271860316975714 @ -111, 42, 49
306079300032694, 427989224301826, 513125950233791 @ 27, -45, -118
228630268190410, 309422704022485, 252191631029483 @ 103, -28, 102
295502752528152, 303859577583371, 440725467531380 @ 37, 74, -49
93265512282292, 185273162073951, 60893993037175 @ 249, 182, 334
217080240114995, 144708198408208, 210126837106682 @ 302, 57, -25
328008958497806, 269660419929825, 370981371272397 @ -125, -79, -219
485295028668410, 271954106532861, 408677951701401 @ -164, 95, -33
415161087248096, 429195993245475, 358857939441649 @ -128, -127, -14
247525387842882, 149260956903186, 218119433210215 @ -121, 5, -122
229690763553086, 184741340719053, 231774455132133 @ 103, 107, 96
273350576987710, 312461639082487, 239928105070136 @ -45, -378, 35
229103347896952, 169414260542242, 177163739369048 @ 129, -277, 437
310532912817766, 338655048610921, 258544235981612 @ -85, -240, 41
276924819912012, 418403331809591, 461328914015385 @ 52, -55, -86
359444867392510, 191570731706833, 549891673617953 @ -133, 132, -454
359054390071828, 180742993164499, 252759886135601 @ -92, 167, 102
254743588182382, 178206845813611, 241108038121475 @ -13, 19, -31
336524796863062, 334504380156442, 353972465313896 @ -21, 9, 7
277642744390978, 161572118705242, 240215671900424 @ -137, 89, -41
418365251578258, 311993365463803, 228954146199587 @ -195, -43, 135
247017809530528, 176454379001059, 250711188563477 @ 40, 73, -20
308064785380155, 232834718037438, 278719003490198 @ -130, -61, -61
146008009553907, 133671901014730, 38210235517724 @ 244, 237, 455
352819526844646, 353013925273785, 294794334396685 @ -78, -82, 43
275861666894518, 206470433361793, 220146999681077 @ -130, -143, 60
210334446212443, 9310396026823, 211561338702080 @ 208, 878, 103
381830088324837, 342678136755254, 233859633492849 @ -166, -131, 120
240359806380076, 144014404706353, 221603259734339 @ 78, 212, 127
293164745657326, 298176993303145, 407724531562325 @ 16, 17, -97
238389055078060, 139355505277517, 149525149574315 @ 78, 218, 323
184863951457574, 222195917005113, 211759500686661 @ 172, 98, 162
219179060778782, 55370821080059, 220941804791635 @ 139, 493, 103
253469056918062, 194315093770291, 243766964231595 @ 19, 15, 13
311228953246370, 217823223654889, 297252581662127 @ -169, -48, -154
238764285805262, 146175061257951, 103074457300905 @ 67, 179, 582
230880907816462, 118825749803017, 159172831887413 @ 104, 404, 640
219822788621262, 172579858603385, 35403285441989 @ 119, 169, 467
321267288021646, 422961112834243, 399808899121358 @ -29, -174, -103
266858090259006, 354840046287825, 351923957469029 @ 5, -349, -226
317592953709487, 176830906385396, 307283590373135 @ -72, 151, -34
197886113356177, 180102793564384, 214180990790690 @ 284, -27, 83
239148185183092, 145711936596641, 206685398747095 @ -15, 40, 22
264761093771686, 237082759979539, 102790214940617 @ 7, -49, 442
218666841311562, 323165165744065, 355297080610573 @ 154, -594, -510
350570942302412, 503545614377236, 351224026806475 @ -31, -165, 18
292610071704572, 276554651620391, 287223335489690 @ -7, -10, 29
300570016134490, 70902094687252, 302175872554043 @ 7, 321, 46
250542727754086, 309402271289725, 214490828930189 @ 15, -534, 104
281484324363906, 270987907706771, 305135166799577 @ 25, 35, 26
128456009294892, 137727869720791, 322302466267420 @ 205, 234, 57
231279746486542, 284772934213321, 205972371856565 @ 99, -386, 144
257823937988715, 157790998443096, 206462318754851 @ -142, 5, 86
211643388234907, 275599597387723, 354859889449466 @ 184, -382, -503
297645490835688, 299741689345597, 267078364272051 @ -22, -66, 57
134130096167034, 272607151747825, 256365127605094 @ 215, 72, 115
260215227767248, 195714104082685, 295389129018935 @ 21, 68, -82
226454221056454, 221984132876617, 352057424140505 @ 117, -96, -397
245204928064672, 188819269848781, 190263217708703 @ -16, -230, 229
343797186510008, 432569014309919, 352014444416655 @ -23, -86, 18
331084804494814, 288546152000179, 207010389233066 @ -45, 14, 171
241763134738462, 200486489662951, 213864982332725 @ 27, -231, 60
306948233883344, 280134969109623, 378698015734343 @ -47, -46, -166
294714522696802, 334062439511041, 260753880231485 @ 8, -50, 94
271796675077915, 96585207614803, 270028331215949 @ -18, 342, -28
371516882302510, 383815105851065, 391949385404489 @ -117, -148, -115
418018339807042, 359655511211741, 388557214865045 @ -156, -71, -76
121697661725341, 193723193175139, 130602515623988 @ 216, 174, 257
306041261138152, 226605576740347, 383793001283928 @ 9, 126, -39
246658692970812, 179205172840811, 235996564286040 @ -7, -86, -93
331361313339152, 81278159656203, 481932100940416 @ -71, 326, -299
183304099697746, 123137916295517, 255584306525969 @ 192, 257, 71
232695697175266, 173188066722133, 260470498627697 @ 86, -139, -411
390945462836707, 398292946600051, 427694512400450 @ -94, -82, -93
203751291129986, 160944522050885, 221624996634685 @ 172, 163, 118
488568022526154, 420718007775775, 302573287334801 @ -203, -99, 62
243370096159912, 168810882348071, 216563758850945 @ -54, -227, -82
273988681663820, 188732258375138, 308515107921018 @ -19, 83, -125
299131842127655, 284890954565020, 439242527017952 @ -62, -123, -391
244498015483452, 203214860662269, 230667098594901 @ -86, -758, -308
277897126459410, 261625585062665, 261606943058794 @ 7, -16, 57
304346254728830, 277451428632005, 308952332265561 @ -25, -7, -5
346630810363762, 121729623133651, 507354255801005 @ -71, 255, -272
342502613959906, 484113405180627, 532120301313849 @ -39, -197, -230
305755448061718, 454071488480319, 458713852477851 @ -33, -331, -279
288618302709196, 248405042253065, 285331293155387 @ -27, -16, -10
223270544071582, 163944467841481, 228451205828405 @ 126, 132, 76
183311641883655, 215117635553996, 110059988469764 @ 148, 155, 275
237792089732986, 212614197700072, 104287625899802 @ 71, -107, 579
269877067447202, 157472117519221, 193473423982615 @ -55, 138, 195
292565528274495, 322445444214329, 223692333990699 @ -112, -416, 90
241859994226702, 132155632738051, 207213284555795 @ -29, 237, 43
258551119695720, 262142379221389, 303200223225513 @ 50, 6, -6
201076392651415, 109026329518666, 261126074212013 @ 132, 265, 116
357365890932622, 177150333541705, 301288545637877 @ -71, 179, 45
223565330173291, 60763596626104, 383802468653225 @ 126, 489, -472
222622622469595, 231570159059665, 189104516040902 @ 140, -232, 217
256518191556091, 59258676112285, 274953029284211 @ -8, 548, -150
297378621823267, 253853338394701, 230030928962390 @ -146, -212, 59
242284556207326, 265111709176964, 394690023851855 @ 51, -341, -682
214057675617562, 18241990446373, 77256662210132 @ 159, 636, 599
238533343423934, 145856883061241, 155612049004581 @ 86, 215, 259
346279238146980, 395510389065632, 320681838564941 @ -55, -113, 20
306937203109996, 353779525358287, 275135723197529 @ 10, -21, 94
219065625240267, 332219246620551, 259718407842977 @ 124, -170, 56
227523894867918, 143879435216005, 213654994666519 @ 163, 36, -126
344141964435022, 343951825236361, 384186561046085 @ -33, -8, -33
221584910749486, 273559980339737, 379968328652101 @ 117, -23, -155
483329585771742, 284970651493017, 314378680779285 @ -176, 73, 58
358747954162366, 214970957445805, 313815073656137 @ -145, 81, -39
427782872755556, 461682706722214, 396594912700694 @ -103, -99, -19
273197692577302, 246483377496385, 231556734274637 @ -21, -88, 84
158970673131942, 295326163963037, 109903141104217 @ 199, 14, 306
248723469812686, 131907658181641, 317333910945653 @ 67, 240, -36
365343487637272, 446801561814751, 195227847662645 @ -116, -265, 188
229053912637580, 115178003768475, 254320146297991 @ 130, 473, -635
259135077129850, 161089433141297, 282109950383439 @ 57, 196, 57
371287905154962, 397637428715581, 267232043549261 @ -146, -225, 62
77112287817025, 154030342833769, 150982478358389 @ 322, 208, 252
272564256792596, 346208933052761, 191130911525403 @ -32, -440, 201
210122568514094, 117636542851169, 150717935513061 @ 311, 383, 634
185977246900926, 272264509576362, 31410773268230 @ 211, -107, 593
298332054101962, 217041486951781, 113861002466405 @ 10, 127, 296
325708253221144, 281586886941808, 505636449588092 @ 5, 91, -121
248147285763122, 102141412399441, 243449165829809 @ 14, 390, -55
287857663578590, 297783824201509, 304526096590465 @ 11, -18, 18
200116244048735, 374877338205221, 302451423846964 @ 158, -220, -15
210933250776428, 65945631766594, 124343281962893 @ 161, 441, 404
257291229319438, 162796294045705, 302968591896629 @ -77, 31, -541
219034927494472, 197329976796415, 311028850130507 @ 134, 53, -143
260179414753440, 261653022009253, 344374387389713 @ -44, -402, -550
293284955142817, 279261212870671, 254315164146860 @ 14, 38, 107
252698228807734, 306825263804709, 425314271385753 @ 33, -299, -521
290984605991992, 356397929922133, 292347752458177 @ 24, -42, 66
249439741374654, 168463492047321, 216925503892597 @ 22, 85, 96
224874514211661, 173250521046782, 203962255310210 @ 110, 169, 173
268043024592682, 191818185465721, 232671927215195 @ -63, -24, 23
241433777528410, 130684280947681, 218961366001469 @ 16, 250, -6
217837911428398, 214658955258340, 289740750415220 @ 131, 43, -37
335459209546298, 284542685455237, 357553987779009 @ -73, -12, -80
225754518967543, 145620873469759, 218260723826183 @ 182, 34, -158
491467628657416, 439494108034806, 407008681987775 @ -159, -65, -22
190463181885161, 109716127912929, 220985873867400 @ 202, 296, 123
277029989037226, 115116345756124, 187440572334869 @ -89, 309, 220
262644144919862, 424470653403921, 273895928979005 @ -23, -898, -118
230506308002572, 217243704246331, 237251338625015 @ 102, -91, 25
219203080606702, 127479547359033, 290633508113381 @ 129, 251, -49
231763043825343, 150756254394880, 109684218694868 @ 98, 201, 365
298167626012347, 343890784063423, 423675682350779 @ 34, 34, -34
322982607364975, 110302272110806, 408400990228217 @ -92, 285, -256
262087688775685, 276759035962173, 308190302722836 @ 42, -28, -21
376374339023502, 185493729289041, 243043111112325 @ -77, 175, 130
239575661381222, 156143580981099, 209034620308791 @ -41, -169, -45
319152630478858, 343770670858030, 249589886064671 @ -137, -329, 42
237690330773152, 151591922873467, 208727783983859 @ 14, -21, 9
351655526618902, 246087626101306, 327110136190010 @ -37, 111, 39
348273020261678, 439015001841373, 498346784261861 @ -77, -222, -268
218075316045983, 275317801447459, 264760038336981 @ 178, -618, -228
314112533570352, 249029366430377, 174038064920275 @ -116, -64, 243
301293927163299, 264980968474550, 200328218440422 @ -52, -47, 177
243951812234622, 189248755691703, 232135239153928 @ 19, -122, -45
205765500189582, 55165589241566, 269777286061575 @ 227, 625, -186
238704412575598, 239702810289417, 217226858296885 @ 72, -152, 108
232442233530894, 174047813539401, 130419194940021 @ 95, 95, 411
270996866100574, 298577713704811, 117566694131636 @ -13, -230, 407
238975771505542, 197751427788641, 244610674867895 @ 63, -68, -43
264303899874352, 212181754108933, 236126991473702 @ -31, -76, 27
237126276582766, 230811458976097, 299247362291297 @ 75, -166, -239
333614586014071, 245305723604038, 194042502031052 @ -160, -47, 191
422365881208882, 219236615679181, 449432931863405 @ -122, 139, -106
197107185588007, 138506497527565, 225158297553086 @ 244, 212, 61
266053445024582, 271995986577745, 311968121326065 @ 29, -42, -47
221690478589702, 32392366896657, 198637365137077 @ 144, 707, 172
266994350369882, 390368607337391, 475305530747785 @ 61, -35, -110
349042137920716, 429664599124959, 337883102326807 @ -24, -71, 39
298704283508254, 298263525225865, 296679721125221 @ -8, -24, 27
251660971267046, 179585166150320, 332801114931047 @ 43, 109, -190
419250207231007, 400436887816591, 297268954923926 @ -216, -210, 17
365714742138785, 305827058151326, 537426018413809 @ -44, 55, -176
269381853934882, 268489058727229, 369325169388137 @ 34, 7, -109
532861043526845, 433488955221944, 511838112993993 @ -202, -61, -128
357947632588747, 306657639824683, 375664958885786 @ -146, -98, -161
232404801802420, 245538245085319, 262356148176699 @ 96, -63, 9
259026112970727, 209418475521332, 232640690212288 @ -56, -193, -21
218525683184894, 394163084821778, 360233541627716 @ 115, -89, -19
278999209023001, 216118474422451, 264467852127311 @ -54, -30, -34
326286404372227, 109008617563040, 380856240762368 @ -96, 287, -193
489391903974223, 224519329306789, 464487706304279 @ -202, 132, -126
188222403544810, 318242021601895, 221953095005789 @ 157, -11, 152"""
