'''
Largest Olympics


Last Updated: June 2025

Medium
ID 9942

96

Find the Olympics with the highest number of unique athletes. The Olympics game is a combination of the year and the season, and is found in the games column. Output the Olympics along with the corresponding number of athletes. The id column uniquely identifies an athlete.

Table
olympics_athletes_events
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

games	athletes_count
1924 Summer	118
olympics_athletes_events
Preview
id	name	sex	age	height	weight	team	noc	games	year	season	city	sport	event	medal
3520	Guillermo J. Amparan	M				Mexico	MEX	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's 800 metres	
35394	Henry John Finchett	M				Great Britain	GBR	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Rings	
21918	Georg Frederik Ahrensborg Clausen	M	28			Denmark	DEN	1924 Summer	1924	Summer	Paris	Cycling	Cycling Men's Road Race Individual	
110345	Marinus Cornelis Dick Sigmond	M	26			Netherlands	NED	1924 Summer	1924	Summer	Paris	Football	Football Men's Football	
54193	Thodore Tho Jeitz	M	26			Luxembourg	LUX	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Individual All-Around	
23240	Charles Barney Cory	M	47	180		United States	USA	1904 Summer	1904	Summer	St. Louis	Golf	Golf Men's Individual	
85019	Nicolaas Johannes Nederpeld	M	37			Netherlands	NED	1924 Summer	1924	Summer	Paris	Fencing	Fencing Men's Foil Individual	
25934	Jan Johannes de Blcourt	M	47			Netherlands	NED	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Free Pistol 50 yards	
35191	John Charles Field-Richards	M	29			Gyrinus-1	GBR	1908 Summer	1908	Summer	London	Motorboating	Motorboating Mixed B-Class (Under 60 Feet)	Gold
4073	Andreac	M				France	FRA	1900 Summer	1900	Summer	Paris	Fencing	Fencing Men's epee Individual	
120786	Pierre Tolar	M				Luxembourg	LUX	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Rings	
33723	August Oliver Gus Fager (Fagerstrm-)	M	32	178	61	United States	USA	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's Cross-Country Team	Silver
82480	Mosso	M				France	FRA	1900 Summer	1900	Summer	Paris	Fencing	Fencing Men's epee Individual	
18257	Gustaf Vilhelm Carlberg	M	44			Sweden	SWE	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Rapid-Fire Pistol 25 metres	Silver
27874	Destin Destine	M				Haiti	HAI	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Free Rifle 400 600 and 800 metres Team	Bronze
5831	Sidney James Montford Sid Atkinson	M	23	186	76	South Africa	RSA	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's 110 metres Hurdles	Silver
72917	Jaroslav Mach	M	37			Czechoslovakia	TCH	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Free Rifle 400 600 and 800 metres Team	
97418	Edmund John Pueschel	M	21			United States	USA	1904 Summer	1904	Summer	St. Louis	Gymnastics	Gymnastics Men's Individual All-Around Apparatus Work	
49768	Dora Honnywill (Neve-)	F	37			Great Britain	GBR	1908 Summer	1908	Summer	London	Archery	Archery Women's Double National Round	
63311	Jan Koutn	M	26			Czechoslovakia	TCH	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Rope Climbing	
81214	Englebert Mollin	M				Belgium	BEL	1924 Summer	1924	Summer	Paris	Wrestling	Wrestling Men's Lightweight Greco-Roman	
26259	Louis Verrant Gabriel Le Bailly de la Falaise	M	42			France	FRA	1908 Summer	1908	Summer	London	Fencing	Fencing Men's Sabre Individual	
100458	Leslie George Rich	M	21			United States	USA	1908 Summer	1908	Summer	London	Swimming	Swimming Men's 100 metres Freestyle	
25585	Henry D. Davids	M				Great Britain	GBR	1908 Summer	1908	Summer	London	Fencing	Fencing Men's epee Individual	
66696	Lucien lie Larg (Barreau-)	M	26			France	FRA	1900 Summer	1900	Summer	Paris	Fencing	Fencing Men's Foil Masters Individual	
47952	Helmer Hermansen	M	29			Norway	NOR	1900 Summer	1900	Summer	Paris	Shooting	Shooting Men's Free Rifle Kneeling 300 metres	
129248	Karl Magnus Wegelius	M	23			Finland	FIN	1908 Summer	1908	Summer	London	Gymnastics	Gymnastics Men's Team All-Around	Bronze
25610	Charles C. Davies	M				Great Britain	GBR	1908 Summer	1908	Summer	London	Athletics	Athletics Men's 400 metres	
13249	tienne Bonnes	M	29	172	76	France	FRA	1924 Summer	1924	Summer	Paris	Rugby	Rugby Men's Rugby	Silver
2723	Gaston Jules Louis Antoine Alibert	M	22			France	FRA	1900 Summer	1900	Summer	Paris	Fencing	Fencing Men's epee Individual	
123217	Fridrihs Uksti	M				Latvia	LAT	1924 Summer	1924	Summer	Paris	Cycling	Cycling Men's Team Pursuit 4000 metres	
51315	Richard Hutton	M				Great Britain	GBR	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Trap	
133878	Ricardo Zamora Martnez	M	23			Spain	ESP	1924 Summer	1924	Summer	Paris	Football	Football Men's Football	
6144	Charles Avrillon	M				France	FRA	1908 Summer	1908	Summer	London	Cycling	Cycling Men's Tandem Sprint 2000 metres	
66748	Jos-Mara Larrabeiti Eguidazu	M	23	173	72	Spain	ESP	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's 200 metres	
63503	Stanisaw Bolesaw Kowalczewski	M	34			Poland	POL	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Free Rifle 400 600 and 800 metres Team	
115057	Thophilus Gerardus Gerard Steurs	M	22			Belgium	BEL	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's Marathon	
99201	John Joseph Joe Ravannack	M	26			Independent Rowing Club-3	USA	1904 Summer	1904	Summer	St. Louis	Rowing	Rowing Men's Double Sculls	Bronze
33350	Fred Rudolph Etchen Sr.	M	39	183		United States	USA	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Trap Team	Gold
44725	John Percival Percy Hagerman	M	22	176		Canada	CAN	1904 Summer	1904	Summer	St. Louis	Athletics	Athletics Men's Triple Jump	
87211	Riccardo Nowak	M	23			Italy	ITA	1908 Summer	1908	Summer	London	Fencing	Fencing Men's epee Team	
48256	Max Hess	M	26	165	71	United States	USA	1904 Summer	1904	Summer	St. Louis	Gymnastics	Gymnastics Men's Individual All-Around	
115954	Albert Stdemann	M				Germany	GER	1908 Summer	1908	Summer	London	Hockey	Hockey Men's Hockey	
98018	Frank K. Raad	M				United States	USA	1904 Summer	1904	Summer	St. Louis	Gymnastics	Gymnastics Men's Individual All-Around Apparatus Work	
22877	Emma C. Cooke	F	55			United States	USA	1904 Summer	1904	Summer	St. Louis	Archery	Archery Women's Double Columbia Round	Silver
3493	Edward John Amoore	M	31			Great Britain	GBR	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Small-Bore Rifle Moving Target 25 yards	
130434	Louis Eugne Edmond Wilhelme	M	23			France	FRA	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's Triple Jump	
128354	Gottlob Friedrich Walz	M	26			Germany	GER	1908 Summer	1908	Summer	London	Diving	Diving Men's Springboard	Bronze
3325	Santiago Amat Cansino	M	36			Amolgavar	ESP	1924 Summer	1924	Summer	Paris	Sailing	Sailing Mixed 6 metres	
85547	Sybil Fenton Newall	F	53			Great Britain	GBR	1908 Summer	1908	Summer	London	Archery	Archery Women's Double National Round	Gold
106413	Ole Andreas Sther	M	38			Norway	NOR	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Free Rifle Three Positions 300 metres Team	Gold
126142	Sotirios Versis	M				Greece	GRE	1900 Summer	1900	Summer	Paris	Athletics	Athletics Men's Shot Put	
121884	Tryfon Triantafyllakos	M				Greece	GRE	1924 Summer	1924	Summer	Paris	Fencing	Fencing Men's Sabre Team	
85860	George Nicol	M	21			Great Britain	GBR	1908 Summer	1908	Summer	London	Athletics	Athletics Men's 400 metres	
68934	Mario Lertora	M	26	165		Italy	ITA	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Horse Vault	
55651	E. J. Jones	M				Cornwall	GBR	1908 Summer	1908	Summer	London	Rugby	Rugby Men's Rugby	Silver
122748	Bertrand Turnbull	M	21			Wales-4	GBR	1908 Summer	1908	Summer	London	Hockey	Hockey Men's Hockey	Bronze
13725	Gerard Dagobert Henri Bosch van Drakestein	M	20			Netherlands	NED	1908 Summer	1908	Summer	London	Cycling	Cycling Men's 100 kilometres	
120119	Benjamin Leonard Ben Thrash	M	26	175		United States	USA	1924 Summer	1924	Summer	Paris	Diving	Diving Men's Plain High	
130983	Jerry Elmer Winholtz	M	29			United States	USA	1904 Summer	1904	Summer	St. Louis	Wrestling	Wrestling Men's Lightweight Freestyle	
53528	Benjamin Jamieson	M	30		75	Winnipeg Shamrocks-1	CAN	1904 Summer	1904	Summer	St. Louis	Lacrosse	Lacrosse Men's Lacrosse	Gold
129432	Ottokar Weise	M				Aschenbrodel	GER	1900 Summer	1900	Summer	Paris	Sailing	Sailing Mixed Open	Silver
126443	Maria Rie Vierdag (-Smit)	F	18	170		Netherlands	NED	1924 Summer	1924	Summer	Paris	Swimming	Swimming Women's 400 metres Freestyle	
66966	August Lass	M	20	177	71	Estonia	EST	1924 Summer	1924	Summer	Paris	Football	Football Men's Football	
125020	Albertson Van Zo Post	M	37	183		United States	USA	1904 Summer	1904	Summer	St. Louis	Fencing	Fencing Men's Foil Team	Gold
129495	John Weldon	M	33			Ireland	IRL	1924 Summer	1924	Summer	Paris	Art Competitions	Art Competitions Mixed Literature	
48394	Henry Hiatt	M				Great Britain	GBR	1900 Summer	1900	Summer	Paris	Gymnastics	Gymnastics Men's Individual All-Around	
115209	Stuart Grosvenor Stu Stickney	M	27			United States	USA	1904 Summer	1904	Summer	St. Louis	Golf	Golf Men's Individual	
2829	Richard Louis Pierre Allemane	M	18			USFSA	FRA	1900 Summer	1900	Summer	Paris	Football	Football Men's Football	Silver
10514	Gustaf Eugen Bergman	M	26			Sweden	SWE	1924 Summer	1924	Summer	Paris	Boxing	Boxing Men's Featherweight	
29107	Hugh Lawrence Laurie Doherty	M	24	178		Great Britain	GBR	1900 Summer	1900	Summer	Paris	Tennis	Tennis Men's Singles	Gold
49580	Martin Drummond Vesey Holt	M	43			Great Britain	GBR	1924 Summer	1924	Summer	Paris	Fencing	Fencing Men's epee Team	
127393	Herbert von Petersdorff	M	19			Germany	GER	1900 Summer	1900	Summer	Paris	Water Polo	Water Polo Men's Water Polo	
124979	Eduardus Ludovicus van Voorst tot Voorst	M	33			Netherlands	NED	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Trap Team	
76076	Claude-Lon Mascaux	M	41			France	FRA	1924 Summer	1924	Summer	Paris	Art Competitions	Art Competitions Mixed Sculpturing	Bronze
56960	Nikolaos Kaloudis	M				Greece	GRE	1924 Summer	1924	Summer	Paris	Water Polo	Water Polo Men's Water Polo	
27905	Christian Jacob Deubler	M	23			Germany	GER	1904 Summer	1904	Summer	St. Louis	Gymnastics	Gymnastics Men's Individual All-Around	
119446	Louis Ren Texier	M	41			France	FRA	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Trap Team	
75884	Antnio Augusto da Silva Martins	M	32			Portugal	POR	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's Discus Throw	
33484	Richmond Cavill Dick Eve	M	23	168		Australia	AUS	1924 Summer	1924	Summer	Paris	Diving	Diving Men's Springboard	
125020	Albertson Van Zo Post	M	37	183		United States	USA	1904 Summer	1904	Summer	St. Louis	Fencing	Fencing Men's Foil Individual	Silver
49855	Thomas Hopkins	M				Great Britain	GBR	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Side Horse	
129575	Jean Welter Sr.	M	23			Luxembourg	LUX	1924 Summer	1924	Summer	Paris	Boxing	Boxing Men's Light-Heavyweight	
50023	Marcel Horsch	M			74	Belgium	BEL	1924 Summer	1924	Summer	Paris	Weightlifting	Weightlifting Men's Middleweight	
7426	George A. Bamber	M				Great Britain	GBR	1924 Summer	1924	Summer	Paris	Art Competitions	Art Competitions Mixed Painting	
77749	Burt Plumb McKinnie	M	25			Trans-Mississippi Golf Association-2	USA	1904 Summer	1904	Summer	St. Louis	Golf	Golf Men's Team	Silver
68934	Mario Lertora	M	26	165		Italy	ITA	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Pommelled Horse	
13447	Claes Arne Borg	M	22			Sweden	SWE	1924 Summer	1924	Summer	Paris	Swimming	Swimming Men's 1500 metres Freestyle	Silver
42295	William Evans Graham	M	22			Ireland-2	GBR	1908 Summer	1908	Summer	London	Hockey	Hockey Men's Hockey	Silver
74446	Jean-Baptiste Manhs	M	27	183	79	France	FRA	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's Marathon	
46989	Lacey Earnest Hearn	M	23			United States	USA	1904 Summer	1904	Summer	St. Louis	Athletics	Athletics Men's 1500 metres	Bronze
17070	Bror Erik Bylhn	M	26	172	61	Sweden	SWE	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's 400 metres	
55942	Jhannes Jsefsson (- Borg)	M	24	174		Iceland	ISL	1908 Summer	1908	Summer	London	Wrestling	Wrestling Men's Middleweight Greco-Roman	
3365	Ernesto Ambrosini	M	29			Italy	ITA	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's 3000 metres Steeplechase	
113507	Koloman Sovi	M	24			Yugoslavia	YUG	1924 Summer	1924	Summer	Paris	Cycling	Cycling Men's Road Race Individual	
116147	Josef Sucharda	M	41			Czechoslovakia	TCH	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Running Target Double Shot	
42822	John William Grieb	M	24	175		United States	USA	1904 Summer	1904	Summer	St. Louis	Gymnastics	Gymnastics Men's Individual All-Around	
70715	Martti Johannes Liuttula	M	30			Finland	FIN	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Running Target Single Shot	
77408	Edward D'Arcy McCrea	M	28			Ireland	IRL	1924 Summer	1924	Summer	Paris	Tennis	Tennis Men's Singles	
123302	Charles Umbs	M	28			United States	USA	1904 Summer	1904	Summer	St. Louis	Gymnastics	Gymnastics Men's Individual All-Around Field Sports	
11132	Emil Beyer	M	27			United States	USA	1904 Summer	1904	Summer	St. Louis	Gymnastics	Gymnastics Men's Individual All-Around Field Sports	
10530	Sidney Bergmann	M				Austria	AUT	1924 Summer	1924	Summer	Paris	Wrestling	Wrestling Men's Lightweight Greco-Roman	
119590	Alexandros Theofilakis	M				Greece	GRE	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Free Pistol 50 yards	
14719	Rene Brasseur	F	21			Luxembourg	LUX	1924 Summer	1924	Summer	Paris	Swimming	Swimming Women's 100 metres Backstroke	
115606	Andrew John Andy Straden	M	26			United States	USA	1924 Summer	1924	Summer	Paris	Football	Football Men's Football	
30187	Andr du Bosch	M				Belgium	BEL	1908 Summer	1908	Summer	London	Fencing	Fencing Men's Sabre Team	
47254	John C. Hein	M	18			United States	USA	1904 Summer	1904	Summer	St. Louis	Wrestling	Wrestling Men's Light-Flyweight Freestyle	Silver
3818	Gerald C. Anderson	M				Great Britain	GBR	1908 Summer	1908	Summer	London	Cycling	Cycling Men's Sprint	
38835	Otto Garnus	M				Switzerland	SUI	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's Shot Put	
87390	Paavo Johannes Nurmi	M	26	174	65	Finland	FIN	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's 1500 metres	Gold
130936	Walter Winans	M	56			United States	USA	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Small-Bore Rifle Disappearing Target 25 yards	
37932	Paul Gailly	M	29			Belgium	BEL	1924 Summer	1924	Summer	Paris	Water Polo	Water Polo Men's Water Polo	Silver
88943	Oscar G. Olson	M				United States	USA	1904 Summer	1904	Summer	St. Louis	Weightlifting	Weightlifting Men's Unlimited Two Hands	
41722	Harold Goodworth	M				Great Britain	GBR	1908 Summer	1908	Summer	London	Diving	Diving Men's Platform	
120786	Pierre Tolar	M				Luxembourg	LUX	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Side Horse	
92116	John Neil Patterson	M	22			United States	USA	1908 Summer	1908	Summer	London	Athletics	Athletics Men's High Jump	
55169	Oskar Emil Johansson	M	23			Sweden	SWE	1908 Summer	1908	Summer	London	Tug-Of-War	Tug-Of-War Men's Tug-Of-War	
112278	Herbert Smith	M	30			Great Britain	GBR	1908 Summer	1908	Summer	London	Football	Football Men's Football	Gold
129828	Edvard Vilhelm Westerlund	M	23	174	77.5	Finland	FIN	1924 Summer	1924	Summer	Paris	Wrestling	Wrestling Men's Middleweight Greco-Roman	Gold
92249	Georges Marie Nestor Pauwels	M	20			Belgium-1	BEL	1900 Summer	1900	Summer	Paris	Equestrianism	Equestrianism Mixed Four-In-Hand Competition	
24838	Edward Martin Dahl	M	21			Sweden	SWE	1908 Summer	1908	Summer	London	Athletics	Athletics Men's 800 metres	
30732	A. Duponcheel	M				France	FRA	1908 Summer	1908	Summer	London	Gymnastics	Gymnastics Men's Team All-Around	
12323	Teodor Tore Blom	M	20			Sweden	SWE	1900 Summer	1900	Summer	Paris	Athletics	Athletics Men's Long Jump	
129642	Charles Sven Otto Wennergren	M	35			Sweden	SWE	1924 Summer	1924	Summer	Paris	Tennis	Tennis Men's Singles	
120168	Georges Thurnherr	M	22	175	66	France	FRA	1908 Summer	1908	Summer	London	Gymnastics	Gymnastics Men's Individual All-Around	
25911	Jan Danil Hendrik de Beaufort	M	27			Netherlands	NED	1908 Summer	1908	Summer	London	Fencing	Fencing Men's Sabre Individual	
115967	Theodore Frederick Ted Studier	M	22			United States	USA	1904 Summer	1904	Summer	St. Louis	Gymnastics	Gymnastics Men's Individual All-Around Apparatus Work	
108863	Giacomo Serra	M				Italy	ITA	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Trap Team	
12814	Erik Viktor Bohlin	M	26			Sweden	SWE	1924 Summer	1924	Summer	Paris	Cycling	Cycling Men's Road Race Team	Bronze
70330	Alois F. Linka	M	25	172	62	Czechoslovakia	TCH	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's 100 metres	
40972	A. Godinat	M				France	FRA	1924 Summer	1924	Summer	Paris	Art Competitions	Art Competitions Mixed Literature	
27423	mile Joseph Demangel	M	25	173	64	France	FRA	1908 Summer	1908	Summer	London	Cycling	Cycling Men's Sprint	Silver
66754	Roberto Larraz	M	25	168		Argentina	ARG	1924 Summer	1924	Summer	Paris	Fencing	Fencing Men's Foil Team	
4404	Johan August Anker	M	36			Fram	NOR	1908 Summer	1908	Summer	London	Sailing	Sailing Mixed 8 metres	
86143	Isidor Gadar Jack Niflot	M	23			United States	USA	1904 Summer	1904	Summer	St. Louis	Wrestling	Wrestling Men's Bantamweight Freestyle	Gold
31220	Ernest Walter Ebbage	M	34			K Division Metropolitan Police Team-3	GBR	1908 Summer	1908	Summer	London	Tug-Of-War	Tug-Of-War Men's Tug-Of-War	Bronze
134205	Juozas ebrauskas	M	19			Lithuania	LTU	1924 Summer	1924	Summer	Paris	Football	Football Men's Football	
53253	Victor Jacquemin	M	16			Belgium	BEL	1908 Summer	1908	Summer	London	Athletics	Athletics Men's 100 metres	
13073	Simon Bon	M	20			Netherlands	NED	1924 Summer	1924	Summer	Paris	Rowing	Rowing Men's Coxed Eights	
22085	Robert Bobby Cloughen	M	19	179	76	United States	USA	1908 Summer	1908	Summer	London	Athletics	Athletics Men's 200 metres	Silver
54686	Marion Hall Jessup (Zinderstein- -MacLure)	F	27	163		United States	USA	1924 Summer	1924	Summer	Paris	Tennis	Tennis Women's Singles	
93221	Giulia Perelli	F				Italy	ITA	1924 Summer	1924	Summer	Paris	Tennis	Tennis Women's Singles	
107550	George Schroeder	M				United States	USA	1904 Summer	1904	Summer	St. Louis	Gymnastics	Gymnastics Men's Individual All-Around Apparatus Work	
25685	Gladys Mary Davis	F	30			Great Britain	GBR	1924 Summer	1924	Summer	Paris	Fencing	Fencing Women's Foil Individual	Silver
26974	Peter Deer	M	25			Canada	CAN	1904 Summer	1904	Summer	St. Louis	Athletics	Athletics Men's 1500 metres	
66681	Allan Edward Lard	M	37			United States	USA	1904 Summer	1904	Summer	St. Louis	Golf	Golf Men's Individual	
51135	Marcus Latimer Hurley	M	20	181		United States	USA	1904 Summer	1904	Summer	St. Louis	Cycling	Cycling Men's 5 mile	
116681	Henri Lon Victor Susse	M	55			Favorite-17	FRA	1900 Summer	1900	Summer	Paris	Sailing	Sailing Mixed Open	
88281	Per Erik Fabian Ohlsson	M	23	173		Sweden	SWE	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Free Rifle 1000 Yards	
26055	Maurice Henri mile de Conninck	M	26			France	FRA	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's 3000 metres Steeplechase	
50961	Jules Guillaume Hulsmans	M	25			Belgium	BEL	1924 Summer	1924	Summer	Paris	Modern Pentathlon	Modern Pentathlon Men's Individual	
121142	Rasmus Aage Ejnar Torgensen	M	24			Denmark	DEN	1924 Summer	1924	Summer	Paris	Wrestling	Wrestling Men's Featherweight Freestyle	
58305	Jzef Ignacy Kaua	M	28	164	66	Poland	POL	1924 Summer	1924	Summer	Paris	Football	Football Men's Football	
17975	James Cantion	M				Moseley Wanderers	GBR	1900 Summer	1900	Summer	Paris	Rugby	Rugby Men's Rugby	Silver
81433	Edwin Herbert Montague	M	23			Great Britain	GBR	1908 Summer	1908	Summer	London	Athletics	Athletics Men's 400 metres	
75956	Charles Louis Marty	M	34			France	FRA	1900 Summer	1900	Summer	Paris	Fencing	Fencing Men's Foil Masters Individual	
39588	Ioannis Georgiadis	M	48			Greece	GRE	1924 Summer	1924	Summer	Paris	Fencing	Fencing Men's Sabre Individual	
16538	Thomas William Bill Burgess	M	27	185	95	Great Britain	GBR	1900 Summer	1900	Summer	Paris	Swimming	Swimming Men's 1000 metres Freestyle	
48898	Stane Hlastan	M				Yugoslavia	YUG	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Rope Climbing	
93893	Peter Geltzer Petersen	M	31			Denmark	DEN	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Free Rifle 400 600 and 800 metres Team	
82090	David Victor Moriaud	M	23			Switzerland	SUI	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's 100 metres	
41856	John Marshall Gorham	M	54			Quicksilver-2	GBR	1908 Summer	1908	Summer	London	Motorboating	Motorboating Mixed B-Class (Under 60 Feet)	
24613	Arthur Ernest D'Anvers	M	25			Belgium	BEL	1924 Summer	1924	Summer	Paris	Rowing	Rowing Men's Coxed Eights	
84580	Jos Nasazzi Yarza	M	22	182	85	Uruguay	URU	1924 Summer	1924	Summer	Paris	Football	Football Men's Football	Gold
26841	Frederick Dean	M	27			Cornwall	GBR	1908 Summer	1908	Summer	London	Rugby	Rugby Men's Rugby	Silver
103259	Joseph Aloysius Joe Ruddy Sr.	M	25			New York Athletic Club #1-1	USA	1904 Summer	1904	Summer	St. Louis	Swimming	Swimming Men's 4 x 50 Yard Freestyle Relay	Gold
112963	John Charles Barney Solomon	M	25			Cornwall	GBR	1908 Summer	1908	Summer	London	Rugby	Rugby Men's Rugby	Silver
78779	Menso Johannes Menso	M	21			Netherlands	NED	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's 400 metres	
125353	Simion Vartolomeu	M	32			Romania	ROU	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Free Rifle 400 600 and 800 metres Team	
86044	Svend Aage Thorvald Michael Nielsen	M	31			Denmark	DEN	1924 Summer	1924	Summer	Paris	Wrestling	Wrestling Men's Middleweight Freestyle	
119794	Albert Henry Harry Thomas	M	19			Great Britain	GBR	1908 Summer	1908	Summer	London	Boxing	Boxing Men's Bantamweight	Gold
76245	Cencio Massola	M				Mebi	ITA	1924 Summer	1924	Summer	Paris	Sailing	Sailing Mixed 6 metres	
72100	Erich Ludwig	M				Frankfurt Club	GER	1900 Summer	1900	Summer	Paris	Rugby	Rugby Men's Rugby	Silver
76221	Gustave Florent Marie Masselin	M	33			France	FRA	1900 Summer	1900	Summer	Paris	Fencing	Fencing Men's Foil Masters Individual	
76928	Ernest Edmund Bedford May	M	29			Great Britain	GBR	1908 Summer	1908	Summer	London	Athletics	Athletics Men's Hammer Throw	
111741	Antonn Skopov	M				Czechoslovakia	TCH	1924 Summer	1924	Summer	Paris	Wrestling	Wrestling Men's Bantamweight Greco-Roman	
94393	Alexandre Emmanuel Pharamond	M	23	164	70	Union des Socits Franais de Sports Athletiques	FRA	1900 Summer	1900	Summer	Paris	Rugby	Rugby Men's Rugby	Gold
96484	Clarkson Potter	M	23			United States	USA	1904 Summer	1904	Summer	St. Louis	Golf	Golf Men's Individual	
27126	Jorge del Mazo	M				Argentina	ARG	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Small-Bore Rifle Prone 50 metres	
70216	Adolf Atte Lindqvist (-Launos)	M	29			Finland	FIN	1924 Summer	1924	Summer	Paris	Diving	Diving Men's Springboard	
8875	Honor Jean Bayard	M	26	173	78	France	FRA	1924 Summer	1924	Summer	Paris	Rugby	Rugby Men's Rugby	Silver
49855	Thomas Hopkins	M				Great Britain	GBR	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Horizontal Bar	
75384	Edward Ed Marsh	M	26			Vesper Boat Club	USA	1900 Summer	1900	Summer	Paris	Rowing	Rowing Men's Coxed Eights	Gold
4285	Andr Angelini	M				France	FRA	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Free Rifle 1000 Yards	
44221	Jean Gutweniger	M	31			Switzerland	SUI	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Team All-Around	Bronze
95402	Clarence Bitters Platt	M	50			United States	USA	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Trap Team	Gold
82362	William Morton	M	27			Canada	CAN	1908 Summer	1908	Summer	London	Cycling	Cycling Men's Sprint	
109597	Martin Joseph Sheridan	M	27	190	88	United States	USA	1908 Summer	1908	Summer	London	Athletics	Athletics Men's Discus Throw Greek Style	Gold
6212	Albert Louis Flix Ayat	M	17	175		France	FRA	1900 Summer	1900	Summer	Paris	Fencing	Fencing Men's epee Masters Individual	
26559	Hlne de Pourtals (Barbey-)	F	32			Lerina	SUI	1900 Summer	1900	Summer	Paris	Sailing	Sailing Mixed Open	
22312	Paul Ren Colas	M	27	170		France	FRA	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Free Rifle Three Positions 300 metres	
41753	Vilm Ladislav Jan Goppold z Lobsdorfu Sr.	M	38			Bohemia	BOH	1908 Summer	1908	Summer	London	Fencing	Fencing Men's epee Individual	
35747	Alfred Edward Flaxman	M	28			Great Britain	GBR	1908 Summer	1908	Summer	London	Athletics	Athletics Men's Discus Throw	
71514	Mogens Lorentzen	M	32			Denmark	DEN	1924 Summer	1924	Summer	Paris	Art Competitions	Art Competitions Mixed Painting	
104899	Salvanahac	M				France	FRA	1900 Summer	1900	Summer	Paris	Fencing	Fencing Men's epee Individual	
32614	Nils Erik Engdahl	M	25	165	57	Sweden	SWE	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's 400 metres	
27429	Jules Demar	M				Societ Nautique de la Marne-3	FRA	1900 Summer	1900	Summer	Paris	Rowing	Rowing Men's Coxed Fours	
26085	Romain Henri Theodor David Reindert de Favauge	M	35			Netherlands	NED	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Trap	
41713	Leo Joseph Budd Goodwin	M	20			New York Athletic Club #1-1	USA	1904 Summer	1904	Summer	St. Louis	Swimming	Swimming Men's 4 x 50 Yard Freestyle Relay	Gold
128837	Watson McLean Watty Washburn	M	29	194		United States-1	USA	1924 Summer	1924	Summer	Paris	Tennis	Tennis Men's Doubles	
125022	Etienne Gustave Frdric Van Zuylen Van Nijevelt Van De Haar	M	39			Belgium-1	BEL	1900 Summer	1900	Summer	Paris	Equestrianism	Equestrianism Mixed Four-In-Hand Competition	
86847	Gustaf Martin Eugen Norberg	M	21			Sweden	SWE	1924 Summer	1924	Summer	Paris	Water Polo	Water Polo Men's Water Polo	
100253	Robert Bob Reynolds	M				United States	USA	1904 Summer	1904	Summer	St. Louis	Gymnastics	Gymnastics Men's Individual All-Around Field Sports	
10287	J. Brard	M				France	FRA	1900 Summer	1900	Summer	Paris	Cycling	Cycling Men's 25 kilometres	
78900	Alexandros Merkati	M	25			Greece	GRE	1900 Summer	1900	Summer	Paris	Golf	Golf Men's Individual	
65839	Franois Jacques Florentin Lafortune	M	28	173	65	Belgium	BEL	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Free Rifle 400 600 and 800 metres Team	
96627	Kenneth Powell	M	23			Great Britain-4	GBR	1908 Summer	1908	Summer	London	Tennis	Tennis Men's Doubles	
46088	Ernest Nason Harmon	M	30	170		United States	USA	1924 Summer	1924	Summer	Paris	Modern Pentathlon	Modern Pentathlon Men's Individual	
48898	Stane Hlastan	M				Yugoslavia	YUG	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Parallel Bars	
52100	Stanislav Indruch	M	24			Czechoslovakia	TCH	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Horizontal Bar	
41936	Bolesaw Gociewicz	M	34			Poland	POL	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Free Rifle 400 600 and 800 metres Team	
14607	Carlos Castello Branco	M		178		Brazil	BRA	1924 Summer	1924	Summer	Paris	Rowing	Rowing Men's Double Sculls	
31394	Gertrude Caroline Trudy Ederle	F	18	167	64	United States	USA	1924 Summer	1924	Summer	Paris	Swimming	Swimming Women's 400 metres Freestyle	Bronze
130318	Hazel Virginia Wightman (Hotchkiss-)	F	37			United States-1	USA	1924 Summer	1924	Summer	Paris	Tennis	Tennis Women's Doubles	Gold
42368	Jules Grandjean	M				Switzerland	SUI	1924 Summer	1924	Summer	Paris	Wrestling	Wrestling Men's Middleweight Greco-Roman	
129215	Thomas Grenfell Wedge	M	26			Cornwall	GBR	1908 Summer	1908	Summer	London	Rugby	Rugby Men's Rugby	Silver
30361	Roger Franois Ducret	M	36			France	FRA	1924 Summer	1924	Summer	Paris	Fencing	Fencing Men's epee Individual	Silver
112308	Joseph M. Joe Smith	M				Great Britain	GBR	1908 Summer	1908	Summer	London	Athletics	Athletics Men's 1500 metres	
47647	L. Hennebicq	M				France	FRA	1908 Summer	1908	Summer	London	Gymnastics	Gymnastics Men's Team All-Around	
126675	Francisco Villota y Baquiola	M	26			Spain	ESP	1900 Summer	1900	Summer	Paris	Basque Pelota	Basque Pelota Men's Two-Man Teams With Cesta	Gold
11050	J. Btout	M				France	FRA	1924 Summer	1924	Summer	Paris	Rowing	Rowing Men's Coxed Eights	
88554	John J. O'Leary	M	43			Great Britain	GBR	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Running Target Single Shot Team	
121960	Giovanni Giorgio Giangiorgio Trissino	M	22			Italy	ITA	1900 Summer	1900	Summer	Paris	Equestrianism	Equestrianism Mixed High Jump	
124149	Cornelis van Altenburg	M	36			Netherlands	NED	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Free Rifle Three Positions 300 metres Team	
32956	Erik Eriksson	M				Sweden	SWE	1900 Summer	1900	Summer	Paris	Swimming	Swimming Men's 200 metres Backstroke	
28418	Jess Diguez Romero	M	21			Spain	ESP	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's Cross-Country Individual	
30927	Albert Duval	M				Martha-1	FRA	1900 Summer	1900	Summer	Paris	Sailing	Sailing Mixed 1-2 Ton	Bronze
36559	Arthur George Fox	M	25			United States	USA	1904 Summer	1904	Summer	St. Louis	Fencing	Fencing Men's Foil Team	Silver
8783	Jean Jacques Baumert	M	21	180	84	France	FRA	1924 Summer	1924	Summer	Paris	Wrestling	Wrestling Men's Light-Heavyweight Greco-Roman	
101050	Viljo Eino Ville Ritola (Koukkari-)	M	28	175	66	Finland	FIN	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's Cross-Country Individual	Silver
115405	Walter Raymond Stokes	M	25	171		United States	USA	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Small-Bore Rifle Prone 50 metres	
45818	Willy Falck Hansen	M	18			Denmark	DEN	1924 Summer	1924	Summer	Paris	Cycling	Cycling Men's 50 kilometres	
5497	George Aschenbrener	M				United States	USA	1904 Summer	1904	Summer	St. Louis	Gymnastics	Gymnastics Men's Individual All-Around Field Sports	
106746	Zoltn Schenker (Ozoray)	M	43			Hungary	HUN	1924 Summer	1924	Summer	Paris	Fencing	Fencing Men's Sabre Individual	
24838	Edward Martin Dahl	M	21			Sweden	SWE	1908 Summer	1908	Summer	London	Athletics	Athletics Men's 5 mile	
100656	Charles Riddy	M	23		77	Argonaut Rowing Club	CAN	1908 Summer	1908	Summer	London	Rowing	Rowing Men's Coxless Fours	Bronze
93846	Willem Wim Peters	M	20	185		Netherlands	NED	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's Triple Jump	
35364	Jeanne Marie Henriette Filleaul-Brohy (Hantjens-)	F	33			France	FRA	1900 Summer	1900	Summer	Paris	Croquet	Croquet Mixed Singles Two Balls	
91682	Johnson Parker-Smith	M	26			Great Britain	GBR	1908 Summer	1908	Summer	London	Lacrosse	Lacrosse Men's Lacrosse	Silver
83360	David Curtiss Munson	M	20			United States	USA	1904 Summer	1904	Summer	St. Louis	Athletics	Athletics Men's 1500 metres	
49688	Asaji Honda	M				Japan	JPN	1924 Summer	1924	Summer	Paris	Tennis	Tennis Men's Singles	
84716	Georg Naue	M				Aschenbrodel	GER	1900 Summer	1900	Summer	Paris	Sailing	Sailing Mixed 1-2 Ton	Gold
48688	Sidney Rae Sid Hinds	M	23	185		United States	USA	1924 Summer	1924	Summer	Paris	Shooting	Shooting Men's Free Rifle 400 600 and 800 metres Team	Gold
69172	Marcel Lvy	M				France	FRA	1900 Summer	1900	Summer	Paris	Fencing	Fencing Men's epee Individual	
96500	Gustave Pottier	M				France	FRA	1908 Summer	1908	Summer	London	Gymnastics	Gymnastics Men's Team All-Around	
37915	George William Gaidzik	M	23	166		United States	USA	1908 Summer	1908	Summer	London	Diving	Diving Men's Springboard	Bronze
53800	Jan Janssen	M	28			Netherlands	NED	1908 Summer	1908	Summer	London	Gymnastics	Gymnastics Men's Individual All-Around	
100799	Walter Riggs	M	47			Emily	GBR	1924 Summer	1924	Summer	Paris	Sailing	Sailing Mixed 8 metres	Silver
29109	Reginald Frank Reggie Doherty	M	27			Great Britain-1	GBR	1900 Summer	1900	Summer	Paris	Tennis	Tennis Men's Doubles	Gold
37138	Heinrich Heinz Freyschmidt	M	20			Germany	GER	1908 Summer	1908	Summer	London	Diving	Diving Men's Springboard	
42827	Hans Grieder	M	22			Switzerland	SUI	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Parallel Bars	
97697	Alfred Harold Pycock	M				Great Britain	GBR	1924 Summer	1924	Summer	Paris	Swimming	Swimming Men's 100 metres Freestyle	
77576	Matthew John Matt McGrath	M	48	182	115	United States	USA	1924 Summer	1924	Summer	Paris	Athletics	Athletics Men's Hammer Throw	Silver
108898	Auguste Serrurier	M	43			France	FRA	1900 Summer	1900	Summer	Paris	Archery	Archery Men's Sur La Perche a La Pyramide	Silver
118921	Leonora Josephine Leonie Taylor	F				United States	USA	1904 Summer	1904	Summer	St. Louis	Archery	Archery Women's Double National Round	
128225	Jesse Alfred Wallingford	M	36			Great Britain	GBR	1908 Summer	1908	Summer	London	Shooting	Shooting Men's Free Rifle Three Positions 300 metres	
56424	Theodore Hartmann Just	M	22			Great Britain	GBR	1908 Summer	1908	Summer	London	Athletics	Athletics Men's 800 metres	
133892	Giorgio Zampori	M	36			Italy	ITA	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Horizontal Bar	
131533	Emily Woodruff (Smiley-)	F	58			United States	USA	1904 Summer	1904	Summer	St. Louis	Archery	Archery Women's Double Columbia Round	
66323	Paul Maximilien Landowski	M	48			France	FRA	1924 Summer	1924	Summer	Paris	Art Competitions	Art Competitions Mixed Sculpturing	
12198	Samuel Sam Blatherwick	M	19			Great Britain	GBR	1908 Summer	1908	Summer	London	Swimming	Swimming Men's 1500 metres Freestyle	
66210	Albert T. E. Lammens	M				Belgium	BEL	1924 Summer	1924	Summer	Paris	Tennis	Tennis Men's Singles	
34244	Adrien Fauchier-Magnan	M	26			France-4	FRA	1900 Summer	1900	Summer	Paris	Tennis	Tennis Men's Doubles	
92407	Ernest Ernie Payne	M	23			Great Britain	GBR	1908 Summer	1908	Summer	London	Cycling	Cycling Men's Sprint	
75868	Francesco Martino	M	23			Italy	ITA	1924 Summer	1924	Summer	Paris	Gymnastics	Gymnastics Men's Rings	Gold
5	Christine Jacoba Aaftink	F	25	185	82	Netherlands	NED	1992 Winter	1992	Winter	Albertville	Speed Skating	Speed Skating Women's 500 metres	
5	Christine Jacoba Aaftink	F	21	185	82	Netherlands	NED	1988 Winter	1988	Winter	Calgary	Speed Skating	Speed Skating Women's 1000 metres	
5	Christine Jacoba Aaftink	F	27	185	82	Netherlands	NED	1994 Winter	1994	Winter	Lillehammer	Speed Skating	Speed Skating Women's 500 metres	
5	Christine Jacoba Aaftink	F	21	185	82	Netherlands	NED	1988 Winter	1988	Winter	Calgary	Speed Skating	Speed Skating Women's 500 metres	
5	Christine Jacoba Aaftink	F	25	185	82	Netherlands	NED	1992 Winter	1992	Winter	Albertville	Speed Skating	Speed Skating Women's 1000 metres	
5	Christine Jacoba Aaftink	F	27	185	82	Netherlands	NED	1994 Winter	1994	Winter	Lillehammer	Speed Skating	Speed Skating Women's 1000 metres	
54601	Jeong Won-Yong	M	20	178	74	South Korea	KOR	2012 Summer	2012	Summer	London	Swimming	Swimming Men's 400 metres Individual Medley	
29914	Theodora Drakou	F	20	169	67	Greece	GRE	2012 Summer	2012	Summer	London	Swimming	Swimming Women's 50 metres Freestyle	
12198	Samuel Sam Blatherwick	M	19			Great Britain	GBR	1908 Summer	1908	Summer	London	Swimming	Swimming Men's 1500 metres Freestyle	
100458	Leslie George Rich	M	21			United States	USA	1908 Summer	1908	Summer	London	Swimming	Swimming Men's 100 metres Freestyle	
12198	Samuel Sam Blatherwick	M	19			Great Britain	GBR	1908 Summer	1908	Summer	London	Swimming	Swimming Men's 1500 metres Freestyle	
86869	Inger Nordb (Kragh-)	F	21			Norway	NOR	1936 Summer	1936	Summer	Berlin	Diving	Diving Women's Platform	
124391	Catharina Maria Toos van der Klaauw (-Steensma)	F	20			Netherlands	NED	1936 Summer	1936	Summer	Berlin	Fencing	Fencing Women's Foil Individual	
70968	Dorothy Brown Locke	F	24			United States	USA	1936 Summer	1936	Summer	Berlin	Fencing	Fencing Women's Foil Individual	
18252	Anne Marie Carl-Nielsen (Brodersen-)	F	73			Denmark	DEN	1936 Summer	1936	Summer	Berlin	Art Competitions	Art Competitions Mixed Sculpturing Unknown Event	
105390	Charles Edward Sands	M	34	181		United States/Great Britain	USA	1900 Summer	1900	Summer	Paris	Tennis	Tennis Men's Doubles	
61099	Sndor Kleckner	M			62	Pannonia RC/National RC	HUN	1908 Summer	1908	Summer	London	Rowing	Rowing Men's Coxed Eights	
86368	August Nilsson	M	27			Denmark/Sweden	SWE	1900 Summer	1900	Summer	Paris	Tug-Of-War	Tug-Of-War Men's Tug-Of-War	Gold
26951	Maxime Omer Mathieu Max Omer-Dcugis	M	17			United States/France	FRA	1900 Summer	1900	Summer	Paris	Tennis	Tennis Men's Doubles	Silver
107090	Eugen Stahl Schmidt	M	38			Denmark/Sweden	DEN	1900 Summer	1900	Summer	Paris	Tug-Of-War	Tug-Of-War Men's Tug-Of-War	Gold
37710	Ole Kristian Furuseth	M	25	182	95	Norway	NOR	1992 Winter	1992	Winter	Albertville	Alpine Skiing	Alpine Skiing Men's Combined	
61011	Marianne Kjrstad	F	23	173	64	Norway	NOR	1994 Winter	1994	Winter	Lillehammer	Alpine Skiing	Alpine Skiing Women's Super G	
111597	Atle Skrdal	M	27	184	83	Norway	NOR	1994 Winter	1994	Winter	Lillehammer	Alpine Skiing	Alpine Skiing Men's Downhill	
39301	Vibecke Caroline Gedde-Dahl	F	20	166	62	Norway	NOR	1994 Winter	1994	Winter	Lillehammer	Alpine Skiing	Alpine Skiing Women's Super G	
71866	Astrid Ldemel	F	20			Norway	NOR	1992 Winter	1992	Winter	Albertville	Alpine Skiing	Alpine Skiing Women's Giant Slalom	
20	Kjetil Andr Aamodt	M	20	176	85	Norway	NOR	1992 Winter	1992	Winter	Albertville	Alpine Skiing	Alpine Skiing Men's Giant Slalom	Bronze
37710	Ole Kristian Furuseth	M	25	182	95	Norway	NOR	1992 Winter	1992	Winter	Albertville	Alpine Skiing	Alpine Skiing Men's Super G	
120092	Jan Einar Thorsen	M	27	181	82	Norway	NOR	1994 Winter	1994	Winter	Lillehammer	Alpine Skiing	Alpine Skiing Men's Super G	
61011	Marianne Kjrstad	F	23	173	64	Norway	NOR	1994 Winter	1994	Winter	Lillehammer	Alpine Skiing	Alpine Skiing Women's Slalom	
75218	Didrik Marksten	M	20			Norway	NOR	1992 Winter	1992	Winter	Albertville	Alpine Skiing	Alpine Skiing Men's Slalom	
45769	Lasse Norman Hansen	M	24	180	73	Denmark	DEN	2016 Summer	2016	Summer	Rio de Janeiro	Cycling	Cycling Men's Team Pursuit 4000 metres	Bronze
14266	Frentorish Tori Bowie	F	25	175	58	United States	USA	2016 Summer	2016	Summer	Rio de Janeiro	Athletics	Athletics Women's 100 metres	Silver
122881	Seremaia Jerry Tuwai Vunisa	M	27	174	81	Fiji	FIJ	2016 Summer	2016	Summer	Rio de Janeiro	Rugby Sevens	Rugby Sevens Men's Rugby Sevens	Gold
118202	Lachlan Tame	M	27	176	80	Australia	AUS	2016 Summer	2016	Summer	Rio de Janeiro	Canoeing	Canoeing Men's Kayak Doubles 1000 metres	Bronze
94406	Michael Fred Phelps II	M	31	193	91	United States	USA	2016 Summer	2016	Summer	Rio de Janeiro	Swimming	Swimming Men's 4 x 200 metres Freestyle Relay	Gold
120074	Victoria Thornley	F	28	193	76	Great Britain	GBR	2016 Summer	2016	Summer	Rio de Janeiro	Rowing	Rowing Women's Double Sculls	Silver
12740	Tijana Bogdanovi	F	18	172	52	Serbia	SRB	2016 Summer	2016	Summer	Rio de Janeiro	Taekwondo	Taekwondo Women's Flyweight	Silver
18610	Hamish Carson	M	27	181	66	New Zealand	NZL	2016 Summer	2016	Summer	Rio de Janeiro	Athletics	Athletics Men's 1500 metres	
90936	Pan Feihong	F	27	173	57	China	CHN	2016 Summer	2016	Summer	Rio de Janeiro	Rowing	Rowing Women's Lightweight Double Sculls	Bronze
4747	Alice Aprot Nawowuna	F	22	152	54	Kenya	KEN	2016 Summer	2016	Summer	Rio de Janeiro	Athletics	Athletics Women's 10000 metres	
122556	Blair Tuke	M	27	181	78	New Zealand	NZL	2016 Summer	2016	Summer	Rio de Janeiro	Sailing	Sailing Men's Skiff	Gold
77716	Emma McKeon	F	22	180	60	Australia	AUS	2016 Summer	2016	Summer	Rio de Janeiro	Swimming	Swimming Women's 4 x 100 metres Freestyle Relay	Gold
106423	Mohamed Karim Moe Sbihi	M	28	202	110	Great Britain	GBR	2016 Summer	2016	Summer	Rio de Janeiro	Rowing	Rowing Men's Coxless Fours	Gold
47672	Josephine Henning	F	26	175	68	Germany	GER	2016 Summer	2016	Summer	Rio de Janeiro	Football	Football Women's Football	Gold
129185	Sam Webster	M	25	183	80	New Zealand	NZL	2016 Summer	2016	Summer	Rio de Janeiro	Cycling	Cycling Men's Team Sprint	Silver
115008	Jan trba	M	35	183	85	Czech Republic	CZE	2016 Summer	2016	Summer	Rio de Janeiro	Canoeing	Canoeing Men's Kayak Fours 1000 metres	Bronze
1478	Rosaria Aiello	F	27	172	74	Italy	ITA	2016 Summer	2016	Summer	Rio de Janeiro	Water Polo	Water Polo Women's Water Polo	Silver
17489	Facundo Callioni	M	30	183	77	Argentina	ARG	2016 Summer	2016	Summer	Rio de Janeiro	Hockey	Hockey Men's Hockey	Gold
10177	Mark Stewart Bennett	M	23	183	89	Great Britain	GBR	2016 Summer	2016	Summer	Rio de Janeiro	Rugby Sevens	Rugby Sevens Men's Rugby Sevens	Silver
19239	Elena Cecchini	F	24	168	55	Italy	ITA	2016 Summer	2016	Summer	Rio de Janeiro	Cycling	Cycling Women's Road Race Individual	
38795	Denis Gargaud Chanut	M	29	181	76	France	FRA	2016 Summer	2016	Summer	Rio de Janeiro	Canoeing	Canoeing Men's Canadian Singles Slalom	Gold
122858	Seda Gurgenovna Tutkhalyan	F	17	146	43	Russia	RUS	2016 Summer	2016	Summer	Rio de Janeiro	Gymnastics	Gymnastics Women's Team All-Around	Silver
48562	Darrell Hill	M	22	191	145	United States	USA	2016 Summer	2016	Summer	Rio de Janeiro	Athletics	Athletics Men's Shot Put	
27574	Deng Wei	F	23	159	63	China	CHN	2016 Summer	2016	Summer	Rio de Janeiro	Weightlifting	Weightlifting Women's Middleweight	Gold
27572	Deng Shudi	M	24	163	58	China	CHN	2016 Summer	2016	Summer	Rio de Janeiro	Gymnastics	Gymnastics Men's Team All-Around	Bronze
24028	Anna Cruz Lebrato	F	29	176	60	Spain	ESP	2016 Summer	2016	Summer	Rio de Janeiro	Basketball	Basketball Women's Basketball	Silver
107368	Jonathan Michael Jon Schofield	M	31	182	80	Great Britain	GBR	2016 Summer	2016	Summer	Rio de Janeiro	Canoeing	Canoeing Men's Kayak Doubles 200 metres	Silver
17755	Veronica Angella Campbell-Brown	F	34	168	58	Jamaica	JAM	2016 Summer	2016	Summer	Rio de Janeiro	Athletics	Athletics Women's 200 metres	
75981	Kei Marumo	F	24	160	50	Japan	JPN	2016 Summer	2016	Summer	Rio de Janeiro	Synchronized Swimming	Synchronized Swimming Women's Team	Bronze
60589	Eliud Kipchoge	M	31	167	57	Kenya	KEN	2016 Summer	2016	Summer	Rio de Janeiro	Athletics	Athletics Men's Marathon	Gold
121635	Lucas Tramr	M	26	183	75	Switzerland	SUI	2016 Summer	2016	Summer	Rio de Janeiro	Rowing	Rowing Men's Lightweight Coxless Fours	Gold
70315	David Thomas Lingmerth	M	29	170	79	Sweden	SWE	2016 Summer	2016	Summer	Rio de Janeiro	Golf	Golf Men's Individual	
34233	Rachel Fattal	F	22	173	65	United States	USA	2016 Summer	2016	Summer	Rio de Janeiro	Water Polo	Water Polo Women's Water Polo	Gold
19603	Kyle Chalmers	M	18	193	90	Australia	AUS	2016 Summer	2016	Summer	Rio de Janeiro	Swimming	Swimming Men's 4 x 100 metres Medley Relay	Bronze
41869	Giulia Gorlero	F	25	180	73	Italy	ITA	2016 Summer	2016	Summer	Rio de Janeiro	Water Polo	Water Polo Women's Water Polo	Silver
79853	Amy Millar	F	39	183	59	Canada	CAN	2016 Summer	2016	Summer	Rio de Janeiro	Equestrianism	Equestrianism Mixed Jumping Individual	
15460	Aaron Brown	M	24	198	79	Canada	CAN	2016 Summer	2016	Summer	Rio de Janeiro	Athletics	Athletics Men's 100 metres	
58866	Isabel Kerschowski	F	28	167	57	Germany	GER	2016 Summer	2016	Summer	Rio de Janeiro	Football	Football Women's Football	Gold
100315	Kimberly Susan Kim Rhode (-Harryman)	F	37	163	82	United States	USA	2016 Summer	2016	Summer	Rio de Janeiro	Shooting	Shooting Women's Skeet	Bronze
23040	Kevin Cordes	M	22	196	88	United States	USA	2016 Summer	2016	Summer	Rio de Janeiro	Swimming	Swimming Men's 100 metres Breaststroke	
91785	Shannon Parry	F	26	170	70	Australia	AUS	2016 Summer	2016	Summer	Rio de Janeiro	Rugby Sevens	Rugby Sevens Women's Rugby Sevens	Gold
39374	Oliver Geis	M	25	176	86	Germany	GER	2016 Summer	2016	Summer	Rio de Janeiro	Shooting	Shooting Men's Rapid-Fire Pistol 25 metres	
105173	Germn Sal Snchez Snchez	M	24	165	50	Mexico	MEX	2016 Summer	2016	Summer	Rio de Janeiro	Diving	Diving Men's Platform	Silver
43150	Marcus Gro	M	26	182	85	Germany	GER	2016 Summer	2016	Summer	Rio de Janeiro	Canoeing	Canoeing Men's Kayak Doubles 1000 metres	Gold
9823	Anastasiya Yevgenyevna Belyakova	F	23	173	60	Russia	RUS	2016 Summer	2016	Summer	Rio de Janeiro	Boxing	Boxing Women's Lightweight	Bronze
118778	Diana Lurena Taurasi	F	34	183	70	United States	USA	2016 Summer	2016	Summer	Rio de Janeiro	Basketball	Basketball Women's Basketball	Gold
48230	Timm Herzbruch	M	19	180	76	Germany	GER	2016 Summer	2016	Summer	Rio de Janeiro	Hockey	Hockey Men's Hockey	Bronze
22299	Massimo Colaci	M	31	180	75	Italy	ITA	2016 Summer	2016	Summer	Rio de Janeiro	Volleyball	Volleyball Men's Volleyball	Silver
124162	Greg Van Avermaet	M	31	181	74	Belgium	BEL	2016 Summer	2016	Summer	Rio de Janeiro	Cycling	Cycling Men's Road Race Individual	Gold
124031	Jean-Charles Valladont	M	27	180	83	France	FRA	2016 Summer	2016	Summer	Rio de Janeiro	Archery	Archery Men's Individual	Silver
122321	Irakli Tsirekidze	M	26	184	90	Georgia	GEO	2008 Summer	2008	Summer	Beijing	Judo	Judo Men's Middleweight	Gold
30576	Alina Alexandra Dumitru (-Croitoru)	F	25	158	48	Romania	ROU	2008 Summer	2008	Summer	Beijing	Judo	Judo Women's Extra-Lightweight	Gold
70384	Soso Lip'art'eliani	M	25	178	78	Georgia	GEO	1996 Summer	1996	Summer	Atlanta	Judo	Judo Men's Half-Middleweight	Bronze
87208	Michel Nowak	M	22	175	77	France	FRA	1984 Summer	1984	Summer	Los Angeles	Judo	Judo Men's Half-Middleweight	Bronze
123132	Masae Ueno	F	25	160	70	Japan	JPN	2004 Summer	2004	Summer	Athina	Judo	Judo Women's Middleweight	Gold
999999	John Testman	M	30	180	75	USA	USA	2000 Summer	2000	Summer	Sydney	Athletics	Athletics Men's 100 metres	 Gold
999998	John Testman	M	30	180	75	Canada	CAN	2004 Summer	2004	Summer	Athens	Athletics	Athletics Men's 200 metres	 Bronze
id:
bigint
name:
string
sex:
string
age:
double
height:
double
weight:
double
team:
string
noc:
string
games:
string
year:
bigint
season:
string
city:
string
sport:
string
event:
string
medal:
string
'''


# Import your libraries
import pyspark
from pyspark.sql import *
from pyspark.sql.functions import *
# Start writing code
# print(olympics_athletes_events.count())
olympics_athletes_events1 =olympics_athletes_events.distinct()
olympics_athletes_events2=olympics_athletes_events1.filter(olympics_athletes_events1.games=="1924 Summer")
# olympics_athletes_events2.show(125,truncate=False)
# print(olympics_athletes_events2.count())
olympics_athletes_events3 = olympics_athletes_events2.dropDuplicates(["id"])
# print(olympics_athletes_events3.count())

olympics_athletes_events3 = olympics_athletes_events3.withColumn("athletes_count",lit(olympics_athletes_events3.count()))
olympics_athletes_events4 = olympics_athletes_events3.select("games","athletes_count")
# To validate your solution, convert your final pySpark df to a pandas df
olympics_athletes_events4.toPandas().head(1)