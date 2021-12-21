TEST: str = """
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
"""

DATA: str = """
--- scanner 0 ---
719,517,-790
-292,-583,-938
-559,608,691
-531,-588,535
566,614,-810
587,611,-765
-537,927,-791
-519,919,-928
663,635,624
-524,-456,650
681,-747,219
648,-740,-624
-506,902,-750
-382,-639,-926
-524,585,668
106,150,-140
697,-786,-622
812,637,728
788,620,506
555,-679,247
708,-617,-651
-508,558,793
-343,-538,-972
19,10,-53
610,-699,219
-654,-581,626

--- scanner 1 ---
480,425,-754
553,914,786
474,851,745
-4,158,-81
666,383,-749
-802,528,-834
692,-584,-776
-689,-595,-559
-749,-306,459
-823,476,-688
-759,-688,-497
-858,672,-736
-838,571,343
-738,-242,425
673,872,699
-645,-249,386
-839,586,306
322,-457,694
696,-354,-767
319,-678,713
556,382,-814
710,-467,-747
-881,617,522
-171,125,48
-763,-671,-530
416,-529,755

--- scanner 2 ---
-841,465,763
327,639,-584
437,681,-607
780,700,525
442,-485,522
798,756,417
280,-417,-522
-123,51,49
-715,-548,344
264,-465,-747
779,782,391
-913,665,787
-525,872,-613
-477,-679,-830
25,-33,-114
-584,827,-563
-629,-774,-784
-787,853,-602
265,-601,-600
486,664,-493
-702,-370,327
411,-546,442
-488,-738,-872
459,-629,430
-684,-507,319
-791,687,738

--- scanner 3 ---
-398,471,621
-729,-747,-426
-626,-677,-316
351,807,-821
-398,-589,705
-653,-587,688
701,-263,-391
836,-387,-426
770,-463,-417
-499,-629,624
747,-348,581
-356,636,-474
34,157,-47
-420,457,444
643,791,475
772,-385,758
784,756,417
723,-476,709
-428,486,484
-377,629,-529
755,718,471
349,774,-745
-624,-790,-375
-45,74,97
-410,599,-420
317,717,-676

--- scanner 4 ---
35,-119,57
-293,400,-792
748,341,837
365,465,-403
817,367,637
-682,376,353
-577,325,310
-493,-733,-416
366,-830,-559
464,491,-457
373,-869,-652
-452,-674,471
-447,-912,-459
819,-808,715
-351,-755,511
-355,351,-741
883,376,713
-579,266,423
-339,522,-702
430,-796,-548
770,-759,624
-30,-32,-98
794,-631,752
-606,-738,513
356,535,-502
-462,-949,-458

--- scanner 5 ---
432,-541,-590
-548,393,-481
789,496,-830
586,-827,665
784,459,-778
386,-451,-468
-466,377,-580
883,607,401
766,432,-873
-573,419,-546
-488,376,493
555,-785,881
540,-784,844
-272,-840,-533
841,727,488
-280,-591,801
28,-15,-36
448,-502,-419
-337,-695,728
-273,-684,762
-371,-786,-559
-560,470,432
820,528,442
-263,-741,-603
-709,373,474

--- scanner 6 ---
618,-574,-411
5,-70,81
714,782,895
794,616,-564
761,559,-485
677,713,875
-705,362,-266
732,-591,-460
-451,-855,-575
612,-383,551
-654,-874,608
623,-402,813
641,-616,-301
676,799,876
-442,-877,-799
662,-428,610
-687,530,889
-563,-953,569
702,633,-584
-728,449,-332
-760,397,876
-784,567,773
-437,-864,-793
-732,354,-224
-546,-898,555

--- scanner 7 ---
535,-835,500
-390,479,-724
-619,-505,787
756,475,-569
94,-140,-155
514,-653,-551
-644,450,358
-715,-807,-717
-570,479,434
775,458,-439
438,-793,351
-284,408,-602
734,380,-523
387,-662,-485
-673,-802,-878
-376,487,-501
815,687,675
-630,-539,723
-59,-83,-57
-526,-466,780
-515,-814,-809
502,-715,-402
829,667,562
441,-774,572
811,696,445
-640,417,341

--- scanner 8 ---
-689,-575,-286
-422,-630,817
-688,681,-696
-72,31,19
582,-727,759
92,-101,-15
-648,-544,-311
-708,528,-599
-517,-782,863
545,-720,609
-458,-771,905
-481,733,790
608,750,-593
65,87,141
382,-705,694
571,520,852
600,632,852
895,-546,-655
830,774,-576
475,528,855
-826,-557,-294
726,625,-578
-663,549,-602
-403,798,862
793,-597,-605
-462,846,742
770,-562,-628

--- scanner 9 ---
700,736,-350
-688,-711,650
-831,-455,-489
554,393,705
-773,433,420
709,-763,-634
585,-410,460
-657,-630,724
611,-311,406
-582,415,-674
-581,446,-716
751,631,-307
-737,318,540
-728,379,331
810,633,-420
-40,-85,-48
541,-302,505
735,-694,-834
725,409,744
-685,-598,585
676,347,795
-825,-396,-417
-550,371,-774
-904,-562,-427
-126,39,54
700,-829,-710

--- scanner 10 ---
408,-788,774
495,387,298
-637,327,-698
705,-734,-891
548,272,381
-765,-855,868
-538,343,-616
-590,-890,-892
-869,245,587
-942,-897,867
-843,-869,726
417,323,-455
-830,291,486
-616,-836,-793
396,-630,705
-920,279,542
-77,-41,40
-660,-791,-901
671,-745,-827
-603,369,-591
403,-830,613
744,-641,-884
436,326,-676
557,399,447
375,420,-604

--- scanner 11 ---
-665,925,853
370,534,769
90,58,154
-657,866,887
647,-401,670
522,498,-551
629,540,-585
-733,617,-301
-728,580,-353
728,-475,701
319,-620,-528
-330,-330,-663
-392,-381,-712
-710,553,-258
-301,-585,750
442,586,735
-701,800,723
-362,-794,741
-23,127,19
604,514,-650
427,-665,-572
-416,-705,786
-376,-420,-541
328,-719,-598
537,478,722
615,-540,698

--- scanner 12 ---
-838,-675,294
447,830,-657
-855,-637,313
372,-623,579
613,-789,-513
494,782,-568
-12,120,-4
518,730,-594
327,-573,638
-453,799,313
-430,-832,-862
-441,-829,-959
-769,-638,314
818,693,581
649,-790,-542
897,602,620
-586,726,300
-703,803,-673
-623,823,416
842,585,634
56,-51,-109
-753,763,-670
346,-584,376
-824,817,-754
731,-737,-553
-491,-681,-873

--- scanner 13 ---
-736,718,685
-782,-766,-442
455,-668,815
437,453,-475
-405,523,-739
-621,-771,-400
883,-469,-496
-713,-778,-600
-384,-473,554
454,486,-471
348,732,506
-506,444,-831
430,-491,778
-572,748,715
436,608,430
443,665,496
876,-430,-589
479,-540,687
-520,-392,545
-81,33,110
-38,-93,-28
530,515,-545
-628,515,-725
-692,818,668
-438,-344,488
819,-503,-485

--- scanner 14 ---
668,-541,-927
458,347,654
-274,648,337
153,-19,-109
-439,-546,725
734,-696,-923
-392,-379,669
-564,860,-895
-497,853,-911
511,436,742
-505,629,-887
-355,-403,-754
923,556,-970
-426,-451,617
-308,656,278
-428,-508,-732
743,-480,-892
-438,692,403
746,-466,586
950,590,-961
-353,-411,-694
527,477,710
890,588,-898
684,-439,549
813,-345,503

--- scanner 15 ---
-690,685,-326
0,-126,136
-546,614,666
801,479,-321
815,261,-312
768,-724,-606
644,-657,502
-525,645,-387
-799,-741,-642
139,-16,4
-532,636,636
618,-487,504
674,450,796
743,-833,-522
-687,-496,840
668,526,827
-733,-646,-738
-521,-603,853
-690,-685,-657
-495,698,-268
798,-569,477
885,-754,-569
-591,-574,885
810,255,-299
-614,538,733
687,493,830

--- scanner 16 ---
439,649,-529
547,677,510
-819,-681,377
328,555,-554
-468,380,-789
578,603,429
275,-745,-456
-810,-757,311
794,-474,578
-601,-409,-829
377,534,-566
575,538,542
-845,-881,446
-695,413,730
715,-464,744
-369,352,-930
3,-10,-137
326,-664,-556
-546,394,-931
-628,-429,-827
-721,359,829
-466,-502,-847
-651,458,838
-150,-63,36
361,-684,-606
721,-536,685

--- scanner 17 ---
-840,-780,-527
520,-721,-748
498,-794,-853
820,-567,419
-766,713,541
-843,-533,-520
764,654,-696
848,-693,351
532,519,510
558,-796,-845
417,512,642
-676,-369,733
-657,371,-544
-56,-72,-99
-844,-748,-551
725,592,-679
-626,-367,626
741,690,-725
-918,752,585
-772,706,630
848,-622,399
-498,258,-527
-794,-366,631
441,642,517
-625,255,-690

--- scanner 18 ---
860,757,-635
-657,-695,838
697,-786,-394
862,-388,914
-816,-746,-728
859,-713,-374
782,-335,900
-768,-689,-646
741,-493,906
-445,366,670
751,579,883
713,540,793
-673,-825,825
695,466,787
888,729,-644
-523,356,585
-792,-804,865
-672,538,-741
-554,464,-637
-663,456,-566
-529,482,611
96,42,78
908,639,-608
724,-806,-392
-687,-680,-782

--- scanner 19 ---
381,-700,-406
-670,-853,-559
-343,-652,555
-537,560,725
594,716,-749
44,-14,-161
-501,531,702
531,831,-830
721,775,686
389,-553,468
-87,21,-2
-421,-674,645
-820,712,-696
831,814,586
-736,-766,-548
340,-775,-491
-933,729,-537
542,651,-913
-636,-769,-385
-599,577,686
372,-626,-430
-407,-491,619
327,-570,284
-936,566,-664
395,-566,341
685,830,708

--- scanner 20 ---
-374,725,-712
765,782,-453
617,-668,-519
737,-481,785
-618,-497,-728
-319,689,-734
587,400,386
736,804,-456
644,446,518
648,-474,779
117,16,99
584,508,405
692,-435,931
-583,-932,638
624,-545,-428
-420,-929,511
-318,535,804
-572,-595,-712
-437,-816,670
-589,-533,-751
-335,835,-612
749,-675,-404
794,618,-458
-433,598,723
-498,546,887

--- scanner 21 ---
-587,-666,-448
664,849,-480
708,-467,-385
640,-729,797
685,-509,-332
-604,717,534
725,396,629
781,378,521
807,397,495
-527,-378,395
-576,911,-496
-585,-511,-435
689,690,-389
-392,896,-418
-49,99,89
-445,-512,423
-521,765,546
-571,-524,-573
661,-809,871
-460,734,626
-440,912,-643
-498,-300,439
706,739,-503
628,-603,904
741,-490,-537
36,-53,166

--- scanner 22 ---
408,671,-922
-417,-537,607
-456,-554,545
-523,514,737
-86,45,-131
657,747,266
740,-356,-804
81,-65,-40
721,724,223
796,-523,-757
-824,883,-632
694,742,318
-840,876,-699
688,-428,-770
760,-590,615
-587,675,801
776,-508,516
349,679,-888
734,-615,550
-661,-485,-768
-497,697,723
-683,-380,-841
-623,-388,-843
-440,-508,643
-816,652,-691
474,715,-758

--- scanner 23 ---
-885,873,575
-613,-333,357
-498,-356,-641
568,-348,-531
459,524,-821
-759,483,-836
-535,-331,-818
650,621,739
-537,-267,366
624,-754,685
377,699,-812
-865,871,548
641,-460,-535
-792,891,710
385,628,-703
567,-786,616
-413,-402,331
-1,97,-118
-626,-380,-769
-825,537,-965
560,657,759
657,-752,761
678,630,711
-768,619,-917
-135,17,11
606,-319,-477

--- scanner 24 ---
-429,-529,446
719,-793,-355
-362,539,638
874,736,-387
-362,737,-682
-580,-591,-350
-493,-690,382
828,600,633
871,515,-406
24,64,-19
520,-814,-401
115,-87,156
640,-856,-314
854,575,568
751,-762,917
870,493,667
-764,-608,-288
815,-739,960
-323,522,576
-462,776,-792
-340,792,-646
788,-757,865
-707,-604,-356
777,587,-345
-346,493,540
-403,-712,460

--- scanner 25 ---
-923,619,-645
391,-828,776
-534,359,557
-875,739,-704
694,782,-649
-758,-819,-419
-899,-673,697
480,-417,-281
-626,-725,-444
14,-1,-6
-523,306,639
341,-853,554
657,523,961
498,-409,-418
-113,-146,127
-605,-722,-399
705,740,-590
467,-434,-459
269,-877,754
598,473,916
-957,-741,793
-494,307,675
553,694,-685
-949,-685,733
-810,667,-626
395,512,942

--- scanner 26 ---
656,-485,-734
743,-443,-614
-497,668,-586
-779,-685,797
-797,-932,-541
-877,-829,741
479,-740,820
-857,-975,-617
263,-771,778
-887,294,844
-792,-974,-727
-94,5,-13
547,496,611
300,-786,777
-927,363,801
468,684,-539
387,633,-560
-547,686,-580
-731,-881,762
632,502,467
558,407,504
-526,702,-701
702,-506,-535
-87,-167,116
-934,486,903
350,715,-645

--- scanner 27 ---
769,361,823
-33,-170,98
-543,-579,585
790,-736,-372
-536,-570,-438
676,-722,779
799,-960,-350
-563,471,-515
905,294,791
-438,556,488
-506,-517,-319
804,-954,-363
-557,-601,615
657,-689,776
587,447,-353
-425,739,585
827,449,757
678,408,-274
-489,383,-436
-701,-530,-377
-568,564,-404
-390,676,580
63,-30,-2
-625,-677,682
663,-765,745
695,394,-329

--- scanner 28 ---
716,745,609
773,-406,687
-574,-322,-360
-604,699,796
711,-445,670
-677,-612,836
-675,-672,844
638,-638,-519
134,-36,-38
-638,751,868
-601,548,-490
-9,-88,101
682,787,716
-541,521,-367
450,869,-569
-448,-350,-428
-591,807,701
399,835,-524
781,771,634
-590,519,-321
809,-429,716
489,823,-468
631,-753,-651
-503,-322,-408
761,-729,-526
-602,-650,739

--- scanner 29 ---
-564,-942,409
-401,374,-500
478,-926,-616
946,-697,556
-380,-865,-739
131,-155,-8
502,-854,-416
921,-728,597
527,-804,-638
-808,473,517
-725,526,402
874,766,-733
-519,-891,375
835,446,678
740,767,-651
848,785,-707
-239,-964,-767
823,398,595
-620,-852,421
-659,535,529
-332,386,-658
743,429,534
-493,381,-700
938,-715,419
-7,-30,130
-238,-787,-725

--- scanner 30 ---
-513,419,-882
486,561,-734
-84,2,-19
-767,302,610
900,-565,560
373,650,401
891,-466,490
-727,-487,743
826,-611,-771
890,-622,-805
437,652,-783
-377,428,-801
-431,362,-930
439,574,392
-765,322,583
-614,-526,-503
883,-715,-844
792,-520,516
-775,-568,-508
-868,-459,842
-706,-726,-496
508,774,366
-785,395,745
91,-105,-102
-869,-501,665
462,689,-606

--- scanner 31 ---
415,510,-798
76,2,-139
655,508,312
547,455,288
438,-893,322
-702,-354,-486
-661,510,758
-352,414,-807
-640,-401,570
-611,451,803
579,-704,-786
-624,-339,-670
566,-661,-820
585,-628,-817
337,355,-832
-617,-511,612
-622,713,784
473,422,-864
452,-675,331
-394,403,-748
-477,-338,-534
-440,555,-843
443,-899,309
-90,-115,-68
564,469,233
-731,-560,595
"""