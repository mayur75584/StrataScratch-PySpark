'''
Find the genre of the person with the most number of oscar winnings


Last Updated: July 2025

Hard
ID 10171

42

Find the genre of the person with the most number of oscar winnings.
If there are more than one person with the same number of oscar wins, return the first one in alphabetic order based on their name. Use the names as keys when joining the tables.

Tables
oscar_nominees
nominee_information
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

top_genre
Drama
oscar_nominees
Preview
year	category	nominee	movie	winner	id
2006	actress in a supporting role	Abigail Breslin	Little Miss Sunshine	FALSE	1
1984	actor in a supporting role	Adolph Caesar	A Soldier's Story	FALSE	2
2006	actress in a supporting role	Adriana Barraza	Babel	FALSE	3
2002	actor in a leading role	Adrien Brody	The Pianist	TRUE	4
1942	actress in a supporting role	Agnes Moorehead	The Magnificent Ambersons	FALSE	5
1944	actress in a supporting role	Agnes Moorehead	Mrs. Parkington	FALSE	6
1948	actress in a supporting role	Agnes Moorehead	Johnny Belinda	FALSE	7
1964	actress in a supporting role	Agnes Moorehead	Hush...Hush, Sweet Charlotte	FALSE	8
1936	actor in a supporting role	Akim Tamiroff	The General Died at Dawn	FALSE	9
1943	actor in a supporting role	Akim Tamiroff	For Whom the Bell Tolls	FALSE	10
1972	actor in a supporting role	Al Pacino	The Godfather	FALSE	11
1973	actor	Al Pacino	Serpico	FALSE	12
1974	actor	Al Pacino	The Godfather Part II	FALSE	13
1975	actor	Al Pacino	Dog Day Afternoon	FALSE	14
1979	actor in a leading role	Al Pacino	...And Justice for All	FALSE	15
1990	actor in a supporting role	Al Pacino	Dick Tracy	FALSE	16
1992	actor in a leading role	Al Pacino	Scent of a Woman	TRUE	17
1992	actor in a supporting role	Al Pacino	Glengarry Glen Ross	FALSE	18
2004	actor in a supporting role	Alan Alda	The Aviator	FALSE	19
1966	actor	Alan Arkin	The Russians Are Coming The Russians Are Coming	FALSE	20
1968	actor	Alan Arkin	The Heart Is a Lonely Hunter	FALSE	21
2006	actor in a supporting role	Alan Arkin	Little Miss Sunshine	TRUE	22
2012	actor in a supporting role	Alan Arkin	Argo	FALSE	23
1968	actor	Alan Bates	The Fixer	FALSE	24
1940	actor in a supporting role	Albert Basserman	Foreign Correspondent	FALSE	25
1987	actor in a supporting role	Albert Brooks	Broadcast News	FALSE	26
1963	actor	Albert Finney	Tom Jones	FALSE	27
1974	actor	Albert Finney	Murder on the Orient Express	FALSE	28
1983	actor in a leading role	Albert Finney	The Dresser	FALSE	29
1984	actor in a leading role	Albert Finney	Under the Volcano	FALSE	30
2000	actor in a supporting role	Albert Finney	Erin Brockovich	FALSE	31
2003	actor in a supporting role	Alec Baldwin	The Cooler	FALSE	32
1952	actor	Alec Guinness	The Lavender Hill Mob	FALSE	33
1957	actor	Alec Guinness	The Bridge on the River Kwai	TRUE	34
1977	actor in a supporting role	Alec Guinness	Star Wars	FALSE	35
1988	actor in a supporting role	Alec Guinness	Little Dorrit	FALSE	36
1944	actor	Alexander Knox	Wilson	FALSE	37
1983	actress in a supporting role	Alfre Woodard	Cross Creek	FALSE	38
1970	actress	Ali MacGraw	Love Story	FALSE	39
1936	actress in a supporting role	Alice Brady	My Man Godfrey	FALSE	40
1937	actress in a supporting role	Alice Brady	In Old Chicago	TRUE	41
1944	actress in a supporting role	Aline MacMahon	Dragon Seed	FALSE	42
2005	actress in a supporting role	Amy Adams	Junebug	FALSE	43
2008	actress in a supporting role	Amy Adams	Doubt	FALSE	44
2010	actress in a supporting role	Amy Adams	The Fighter	FALSE	45
2012	actress in a supporting role	Amy Adams	The Master	FALSE	46
1983	actress in a supporting role	Amy Irving	Yentl	FALSE	47
1985	actress in a supporting role	Amy Madigan	Twice in a Lifetime	FALSE	48
2007	actress in a supporting role	Amy Ryan	Gone Baby Gone	FALSE	49
1937	actress in a supporting role	Andrea Leeds	Stage Door	FALSE	50
1990	actor in a supporting role	Andy Garcia	The Godfather, Part III	FALSE	51
1993	actress in a leading role	Angela Bassett	What's Love Got to Do with It	FALSE	52
1944	actress in a supporting role	Angela Lansbury	Gaslight	FALSE	53
1945	actress in a supporting role	Angela Lansbury	The Picture of Dorian Gray	FALSE	54
1962	actress in a supporting role	Angela Lansbury	The Manchurian Candidate	FALSE	55
1999	actress in a supporting role	Angelina Jolie	Girl, Interrupted	TRUE	56
2008	actress in a leading role	Angelina Jolie	Changeling	FALSE	57
1985	actress in a supporting role	Anjelica Huston	Prizzi's Honor	TRUE	58
1989	actress in a supporting role	Anjelica Huston	Enemies, A Love Story	FALSE	59
1990	actress in a leading role	Anjelica Huston	The Grifters	FALSE	60
1945	actress in a supporting role	Ann Blyth	Mildred Pierce	FALSE	61
1987	actress in a supporting role	Ann Sothern	The Whales of August	FALSE	62
1971	actress in a supporting role	Ann-Margret	Carnal Knowledge	FALSE	63
1975	actress	Ann-Margret	Tommy	FALSE	64
2009	actress in a supporting role	Anna Kendrick	Up in the Air	FALSE	65
1955	actress	Anna Magnani	The Rose Tattoo	TRUE	66
1957	actress	Anna Magnani	Wild Is the Wind	FALSE	67
1993	actress in a supporting role	Anna Paquin	The Piano	TRUE	68
1987	actress in a supporting role	Anne Archer	Fatal Attraction	FALSE	69
1962	actress	Anne Bancroft	The Miracle Worker	TRUE	70
1964	actress	Anne Bancroft	The Pumpkin Eater	FALSE	71
1967	actress	Anne Bancroft	The Graduate	FALSE	72
1977	actress in a leading role	Anne Bancroft	The Turning Point	FALSE	73
1985	actress in a leading role	Anne Bancroft	Agnes of God	FALSE	74
1946	actress in a supporting role	Anne Baxter	The Razor's Edge	TRUE	75
1950	actress	Anne Baxter	All about Eve	FALSE	76
2008	actress in a leading role	Anne Hathaway	Rachel Getting Married	FALSE	77
2012	actress in a supporting role	Anne Hathaway	Les Mis_rables	TRUE	78
1987	actress in a supporting role	Anne Ramsey	Throw Momma from the Train	FALSE	79
1943	actress in a supporting role	Anne Revere	The Song of Bernadette	FALSE	80
1945	actress in a supporting role	Anne Revere	National Velvet	TRUE	81
1947	actress in a supporting role	Anne Revere	Gentleman's Agreement	FALSE	82
1937	actress in a supporting role	Anne Shirley	Stella Dallas	FALSE	83
1990	actress in a supporting role	Annette Bening	The Grifters	FALSE	84
1999	actress in a leading role	Annette Bening	American Beauty	FALSE	85
2004	actress in a leading role	Annette Bening	Being Julia	FALSE	86
2010	actress in a leading role	Annette Bening	The Kids Are All Right	FALSE	87
1966	actress	Anouk Aimee	A Man and a Woman	FALSE	88
1957	actor	Anthony Franciosa	A Hatful of Rain	FALSE	89
1991	actor in a leading role	Anthony Hopkins	The Silence of the Lambs	TRUE	90
1993	actor in a leading role	Anthony Hopkins	The Remains of the Day	FALSE	91
1995	actor in a leading role	Anthony Hopkins	Nixon	FALSE	92
1997	actor in a supporting role	Anthony Hopkins	Amistad	FALSE	93
1956	actor in a supporting role	Anthony Perkins	Friendly Persuasion	FALSE	94
1969	actor in a supporting role	Anthony Quayle	Anne of the Thousand Days	FALSE	95
1952	actor in a supporting role	Anthony Quinn	Viva Zapata!	TRUE	96
1956	actor in a supporting role	Anthony Quinn	Lust for Life	TRUE	97
1957	actor	Anthony Quinn	Wild Is the Wind	FALSE	98
1964	actor	Anthony Quinn	Zorba the Greek	FALSE	99
1996	actor in a supporting role	Armin Mueller-Stahl	Shine	FALSE	100
1974	actor	Art Carney	Harry and Tonto	TRUE	101
1952	actor in a supporting role	Arthur Hunnicutt	The Big Sky	FALSE	102
1949	actor in a supporting role	Arthur Kennedy	Champion	FALSE	103
1951	actor	Arthur Kennedy	Bright Victory	FALSE	104
1955	actor in a supporting role	Arthur Kennedy	Trial	FALSE	105
1957	actor in a supporting role	Arthur Kennedy	Peyton Place	FALSE	106
1958	actor in a supporting role	Arthur Kennedy	Some Came Running	FALSE	107
1955	actor in a supporting role	Arthur O'Connell	Picnic	FALSE	108
1959	actor in a supporting role	Arthur O'Connell	Anatomy of a Murder	FALSE	109
1953	actress	Audrey Hepburn	Roman Holiday	TRUE	110
1954	actress	Audrey Hepburn	Sabrina	FALSE	111
1959	actress	Audrey Hepburn	The Nun's Story	FALSE	112
1961	actress	Audrey Hepburn	Breakfast at Tiffany's	FALSE	113
1967	actress	Audrey Hepburn	Wait until Dark	FALSE	114
1953	actress	Ava Gardner	Mogambo	FALSE	115
1979	actress in a supporting role	Barbara Barrie	Breaking Away	FALSE	116
1948	actress in a supporting role	Barbara Bel Geddes	I Remember Mama	FALSE	117
1971	actress in a supporting role	Barbara Harris	Who Is Harry Kellerman and Why Is He Saying Those Terrible Things about Me?	FALSE	118
1996	actress in a supporting role	Barbara Hershey	The Portrait of a Lady	FALSE	119
1940	actress in a supporting role	Barbara O'Neil	All This, and Heaven Too	FALSE	120
1937	actress	Barbara Stanwyck	Stella Dallas	FALSE	121
1941	actress	Barbara Stanwyck	Ball of Fire	FALSE	122
1944	actress	Barbara Stanwyck	Double Indemnity	FALSE	123
1948	actress	Barbara Stanwyck	Sorry, Wrong Number	FALSE	124
1968	actress	Barbra Streisand	Funny Girl	TRUE	125
1973	actress	Barbra Streisand	The Way We Were	FALSE	126
1944	actor	Barry Fitzgerald	Going My Way	FALSE	127
1944	actor in a supporting role	Barry Fitzgerald	Going My Way	TRUE	128
1936	actor in a supporting role	Basil Rathbone	Romeo and Juliet	FALSE	129
1938	actor in a supporting role	Basil Rathbone	If I Were King	FALSE	130
1967	actress in a supporting role	Beah Richards	Guess Who's Coming to Dinner	FALSE	131
1976	actress in a supporting role	Beatrice Straight	Network	TRUE	132
1971	actor in a supporting role	Ben Johnson	The Last Picture Show	TRUE	133
1982	actor in a leading role	Ben Kingsley	Gandhi	TRUE	134
1991	actor in a supporting role	Ben Kingsley	Bugsy	FALSE	135
2001	actor in a supporting role	Ben Kingsley	Sexy Beast	FALSE	136
2003	actor in a leading role	Ben Kingsley	House of Sand and Fog	FALSE	137
2000	actor in a supporting role	Benicio Del Toro	Traffic	TRUE	138
2003	actor in a supporting role	Benicio Del Toro	21 Grams	FALSE	139
2011	actress in a supporting role	B_r_nice Bejo	The Artist	FALSE	140
1955	actress in a supporting role	Betsy Blair	Marty	FALSE	141
1938	actress	Bette Davis	Jezebel	TRUE	142
1939	actress	Bette Davis	Dark Victory	FALSE	143
1940	actress	Bette Davis	The Letter	FALSE	144
1941	actress	Bette Davis	The Little Foxes	FALSE	145
1942	actress	Bette Davis	Now, Voyager	FALSE	146
1944	actress	Bette Davis	Mr. Skeffington	FALSE	147
1950	actress	Bette Davis	All about Eve	FALSE	148
1952	actress	Bette Davis	The Star	FALSE	149
1962	actress	Bette Davis	What Ever Happened to Baby Jane?	FALSE	150
1979	actress in a leading role	Bette Midler	The Rose	FALSE	151
1991	actress in a leading role	Bette Midler	For the Boys	FALSE	152
1936	actress in a supporting role	Beulah Bondi	The Gorgeous Hussy	FALSE	153
1938	actress in a supporting role	Beulah Bondi	Of Human Hearts	FALSE	154
2003	actor in a leading role	Bill Murray	Lost in Translation	FALSE	155
1938	actress in a supporting role	Billie Burke	Merrily We Live	FALSE	156
1996	actor in a leading role	Billy Bob Thornton	Sling Blade	FALSE	157
1998	actor in a supporting role	Billy Bob Thornton	A Simple Plan	FALSE	158
1944	actor	Bing Crosby	Going My Way	TRUE	159
1945	actor	Bing Crosby	The Bells of St. Mary's	FALSE	160
1954	actor	Bing Crosby	The Country Girl	FALSE	161
1986	actor in a leading role	Bob Hoskins	Mona Lisa	FALSE	162
1963	actor in a supporting role	Bobby Darin	Captain Newman, M.D.	FALSE	163
1936	actress in a supporting role	Bonita Granville	These Three	FALSE	164
1975	actor in a supporting role	Brad Dourif	One Flew over the Cuckoo's Nest	FALSE	165
1995	actor in a supporting role	Brad Pitt	12 Monkeys	FALSE	166
2008	actor in a leading role	Brad Pitt	The Curious Case of Benjamin Button	FALSE	167
2011	actor in a leading role	Brad Pitt	Moneyball	FALSE	168
2012	actor in a leading role	Bradley Cooper	Silver Linings Playbook	FALSE	169
1953	actor in a supporting role	Brandon De Wilde	Shane	FALSE	170
1996	actress in a leading role	Brenda Blethyn	Secrets & Lies	FALSE	171
1998	actress in a supporting role	Brenda Blethyn	Little Voice	FALSE	172
1989	actress in a supporting role	Brenda Fricker	My Left Foot	TRUE	173
1975	actress in a supporting role	Brenda Vaccaro	Jacqueline Susann's Once Is Not Enough	FALSE	174
1939	actor in a supporting role	Brian Aherne	Juarez	FALSE	175
1939	actor in a supporting role	Brian Donlevy	Beau Geste	FALSE	176
1949	actor	Broderick Crawford	All the King's Men	TRUE	177
1990	actor in a supporting role	Bruce Davison	Longtime Companion	FALSE	178
1978	actor in a supporting role	Bruce Dern	Coming Home	FALSE	179
1975	actor in a supporting role	Burgess Meredith	The Day of the Locust	FALSE	180
1976	actor in a supporting role	Burgess Meredith	Rocky	FALSE	181
1958	actor in a supporting role	Burl Ives	The Big Country	TRUE	182
1953	actor	Burt Lancaster	From Here to Eternity	FALSE	183
1960	actor	Burt Lancaster	Elmer Gantry	TRUE	184
1962	actor	Burt Lancaster	Birdman of Alcatraz	FALSE	185
1981	actor in a leading role	Burt Lancaster	Atlantic City	FALSE	186
1997	actor in a supporting role	Burt Reynolds	Boogie Nights	FALSE	187
1976	actor in a supporting role	Burt Young	Rocky	FALSE	188
1979	actress in a supporting role	Candice Bergen	Starting Over	FALSE	189
1973	actress in a supporting role	Candy Clark	American Graffiti	FALSE	190
1958	actress in a supporting role	Cara Williams	The Defiant Ones	FALSE	191
2009	actress in a leading role	Carey Mulligan	An Education	FALSE	192
1967	actress in a supporting role	Carol Channing	Thoroughly Modern Millie	FALSE	193
1975	actress	Carol Kane	Hester Street	FALSE	194
1936	actress	Carole Lombard	My Man Godfrey	FALSE	195
1957	actress in a supporting role	Carolyn Jones	The Bachelor Party	FALSE	196
1970	actress	Carrie Snodgress	Diary of a Mad Housewife	FALSE	197
1956	actress	Carroll Baker	Baby Doll	FALSE	198
1941	actor	Cary Grant	Penny Serenade	FALSE	199
1944	actor	Cary Grant	None but the Lonely Heart	FALSE	200
2007	actor in a supporting role	Casey Affleck	The Assassination of Jesse James by the Coward Robert Ford	FALSE	201
2004	actress in a leading role	Catalina Sandino Moreno	Maria Full of Grace	FALSE	202
1998	actress in a leading role	Cate Blanchett	Elizabeth	FALSE	203
2004	actress in a supporting role	Cate Blanchett	The Aviator	TRUE	204
2006	actress in a supporting role	Cate Blanchett	Notes on a Scandal	FALSE	205
2007	actress in a leading role	Cate Blanchett	Elizabeth: The Golden Age	FALSE	206
2007	actress in a supporting role	Cate Blanchett	I'm Not There	FALSE	207
1969	actress in a supporting role	Catherine Burns	Last Summer	FALSE	208
1992	actress in a leading role	Catherine Deneuve	Indochine	FALSE	209
1999	actress in a supporting role	Catherine Keener	Being John Malkovich	FALSE	210
2005	actress in a supporting role	Catherine Keener	Capote	FALSE	211
2002	actress in a supporting role	Catherine Zeta-Jones	Chicago	TRUE	212
1980	actress in a supporting role	Cathy Moriarty	Raging Bull	FALSE	213
1948	actor in a supporting role	Cecil Kellaway	The Luck of the Irish	FALSE	214
1967	actor in a supporting role	Cecil Kellaway	Guess Who's Coming to Dinner	FALSE	215
1947	actress in a supporting role	Celeste Holm	Gentleman's Agreement	TRUE	216
1949	actress in a supporting role	Celeste Holm	Come to the Stable	FALSE	217
1950	actress in a supporting role	Celeste Holm	All about Eve	FALSE	218
1946	actress	Celia Johnson	Brief Encounter	FALSE	219
1943	actor in a supporting role	Charles Bickford	The Song of Bernadette	FALSE	220
1947	actor in a supporting role	Charles Bickford	The Farmer's Daughter	FALSE	221
1948	actor in a supporting role	Charles Bickford	Johnny Belinda	FALSE	222
1937	actor	Charles Boyer	Conquest	FALSE	223
1938	actor	Charles Boyer	Algiers	FALSE	224
1944	actor	Charles Boyer	Gaslight	FALSE	225
1961	actor	Charles Boyer	Fanny	FALSE	226
1940	actor	Charles Chaplin	The Great Dictator	FALSE	227
1941	actor in a supporting role	Charles Coburn	The Devil and Miss Jones	FALSE	228
1943	actor in a supporting role	Charles Coburn	The More the Merrier	TRUE	229
1946	actor in a supporting role	Charles Coburn	The Green Years	FALSE	230
1982	actor in a supporting role	Charles Durning	The Best Little Whorehouse in Texas	FALSE	231
1983	actor in a supporting role	Charles Durning	To Be or Not to Be	FALSE	232
1957	actor	Charles Laughton	Witness for the Prosecution	FALSE	233
2003	actress in a leading role	Charlize Theron	Monster	TRUE	234
2005	actress in a leading role	Charlize Theron	North Country	FALSE	235
1959	actor	Charlton Heston	Ben-Hur	TRUE	236
1994	actor in a supporting role	Chazz Palminteri	Bullets over Broadway	FALSE	237
1983	actress in a supporting role	Cher	Silkwood	FALSE	238
1987	actress in a leading role	Cher	Moonstruck	TRUE	239
1970	actor in a supporting role	Chief Dan George	Little Big Man	FALSE	240
1960	actor in a supporting role	Chill Wills	The Alamo	FALSE	241
1999	actress in a supporting role	Chlo� Sevigny	Boys Don't Cry	FALSE	242
2002	actor in a supporting role	Chris Cooper	Adaptation	TRUE	243
1975	actor in a supporting role	Chris Sarandon	Dog Day Afternoon	FALSE	244
2010	actor in a supporting role	Christian Bale	The Fighter	TRUE	245
1984	actress in a supporting role	Christine Lahti	Swing Shift	FALSE	246
2009	actor in a supporting role	Christoph Waltz	Inglourious Basterds	TRUE	247
2012	actor in a supporting role	Christoph Waltz	Django Unchained	TRUE	248
2009	actor in a supporting role	Christopher Plummer	The Last Station	FALSE	249
2011	actor in a supporting role	Christopher Plummer	Beginners	TRUE	250
1978	actor in a supporting role	Christopher Walken	The Deer Hunter	TRUE	251
2002	actor in a supporting role	Christopher Walken	Catch Me If You Can	FALSE	252
1972	actress	Cicely Tyson	Sounder	FALSE	253
1937	actress in a supporting role	Claire Trevor	Dead End	FALSE	254
1948	actress in a supporting role	Claire Trevor	Key Largo	TRUE	255
1954	actress in a supporting role	Claire Trevor	The High and the Mighty	FALSE	256
1939	actor	Clark Gable	Gone with the Wind	FALSE	257
1939	actor in a supporting role	Claude Rains	Mr. Smith Goes to Washington	FALSE	258
1943	actor in a supporting role	Claude Rains	Casablanca	FALSE	259
1944	actor in a supporting role	Claude Rains	Mr. Skeffington	FALSE	260
1946	actor in a supporting role	Claude Rains	Notorious	FALSE	261
1944	actress	Claudette Colbert	Since You Went Away	FALSE	262
1968	actor	Cliff Robertson	Charly	TRUE	263
1944	actor in a supporting role	Clifton Webb	Laura	FALSE	264
1946	actor in a supporting role	Clifton Webb	The Razor's Edge	FALSE	265
1948	actor	Clifton Webb	Sitting Pretty	FALSE	266
1992	actor in a leading role	Clint Eastwood	Unforgiven	FALSE	267
2004	actor in a leading role	Clint Eastwood	Million Dollar Baby	FALSE	268
2004	actor in a supporting role	Clive Owen	Closer	FALSE	269
1971	actress in a supporting role	Cloris Leachman	The Last Picture Show	TRUE	270
1952	actress in a supporting role	Colette Marchand	Moulin Rouge	FALSE	271
2009	actor in a leading role	Colin Firth	A Single Man	FALSE	272
2010	actor in a leading role	Colin Firth	The King's Speech	TRUE	273
1945	actor	Cornel Wilde	A Song to Remember	FALSE	274
1996	actor in a supporting role	Cuba Gooding, Jr.	Jerry Maguire	TRUE	275
1963	actress in a supporting role	Dame Edith Evans	Tom Jones	FALSE	276
1964	actress in a supporting role	Dame Edith Evans	The Chalk Garden	FALSE	277
1967	actress	Dame Edith Evans	The Whisperers	FALSE	278
1937	actress in a supporting role	Dame May Whitty	Night Must Fall	FALSE	279
1942	actress in a supporting role	Dame May Whitty	Mrs. Miniver	FALSE	280
1989	actor in a supporting role	Dan Aykroyd	Driving Miss Daisy	FALSE	281
1948	actor	Dan Dailey	When My Baby Smiles at Me	FALSE	282
1954	actor	Dan O'Herlihy	Adventures of Robinson Crusoe	FALSE	283
1989	actor in a leading role	Daniel Day Lewis	My Left Foot	TRUE	284
1993	actor in a leading role	Daniel Day-Lewis	In the Name of the Father	FALSE	285
2002	actor in a leading role	Daniel Day-Lewis	Gangs of New York	FALSE	286
2007	actor in a leading role	Daniel Day-Lewis	There Will Be Blood	TRUE	287
2012	actor in a leading role	Daniel Day-Lewis	Lincoln	TRUE	288
1968	actor in a supporting role	Daniel Massey	Star!	FALSE	289
1989	actor in a supporting role	Danny Aiello	Do the Right Thing	FALSE	290
1958	actor	David Niven	Separate Tables	TRUE	291
1992	actor in a supporting role	David Paymer	Mr. Saturday Night	FALSE	292
2005	actor in a leading role	David Strathairn	Good Night, and Good Luck.	FALSE	293
1949	actor in a supporting role	Dean Jagger	Twelve O'Clock High	TRUE	294
1988	actor in a supporting role	Dean Stockwell	Married to the Mob	FALSE	295
1964	actress	Debbie Reynolds	The Unsinkable Molly Brown	FALSE	296
1949	actress	Deborah Kerr	Edward, My Son	FALSE	297
1953	actress	Deborah Kerr	From Here to Eternity	FALSE	298
1956	actress	Deborah Kerr	The King and I	FALSE	299
1957	actress	Deborah Kerr	Heaven Knows, Mr. Allison	FALSE	300
1958	actress	Deborah Kerr	Separate Tables	FALSE	301
1960	actress	Deborah Kerr	The Sundowners	FALSE	302
1982	actress in a leading role	Debra Winger	An Officer and a Gentleman	FALSE	303
1983	actress in a leading role	Debra Winger	Terms of Endearment	FALSE	304
1993	actress in a leading role	Debra Winger	Shadowlands	FALSE	305
2011	actor in a leading role	Demian Bichir	A Better Life	FALSE	306
1986	actor in a supporting role	Denholm Elliott	A Room with a View	FALSE	307
1986	actor in a supporting role	Dennis Hopper	Hoosiers	FALSE	308
1987	actor in a supporting role	Denzel Washington	Cry Freedom	FALSE	309
1989	actor in a supporting role	Denzel Washington	Glory	TRUE	310
1992	actor in a leading role	Denzel Washington	Malcolm X	FALSE	311
1999	actor in a leading role	Denzel Washington	The Hurricane	FALSE	312
2001	actor in a leading role	Denzel Washington	Training Day	TRUE	313
2012	actor in a leading role	Denzel Washington	Flight	FALSE	314
1986	actor in a leading role	Dexter Gordon	Round Midnight	FALSE	315
1974	actress	Diahann Carroll	Claudine	FALSE	316
1972	actress	Diana Ross	Lady Sings the Blues	FALSE	317
1980	actress in a supporting role	Diana Scarwid	Inside Moves	FALSE	318
1963	actress in a supporting role	Diane Cilento	Tom Jones	FALSE	319
1977	actress in a leading role	Diane Keaton	Annie Hall	TRUE	320
1981	actress in a leading role	Diane Keaton	Reds	FALSE	321
1996	actress in a leading role	Diane Keaton	Marvin's Room	FALSE	322
2003	actress in a leading role	Diane Keaton	Something's Gotta Give	FALSE	323
1974	actress in a supporting role	Diane Ladd	Alice Doesn't Live Here Anymore	FALSE	324
1990	actress in a supporting role	Diane Ladd	Wild at Heart	FALSE	325
1991	actress in a supporting role	Diane Ladd	Rambling Rose	FALSE	326
2002	actress in a leading role	Diane Lane	Unfaithful	FALSE	327
1957	actress in a supporting role	Diane Varsi	Peyton Place	FALSE	328
1986	actress in a supporting role	Dianne Wiest	Hannah and Her Sisters	TRUE	329
1989	actress in a supporting role	Dianne Wiest	Parenthood	FALSE	330
1994	actress in a supporting role	Dianne Wiest	Bullets over Broadway	TRUE	331
2003	actor in a supporting role	Djimon Hounsou	In America	FALSE	332
2006	actor in a supporting role	Djimon Hounsou	Blood Diamond	FALSE	333
1985	actor in a supporting role	Don Ameche	Cocoon	TRUE	334
2004	actor in a leading role	Don Cheadle	Hotel Rwanda	FALSE	335
1956	actor in a supporting role	Don Murray	Bus Stop	FALSE	336
1941	actor in a supporting role	Donald Crisp	How Green Was My Valley	TRUE	337
1953	actress in a supporting role	Donna Reed	From Here to Eternity	TRUE	338
1959	actress	Doris Day	Pillow Talk	FALSE	339
1954	actress	Dorothy Dandridge	Carmen Jones	FALSE	340
1956	actress in a supporting role	Dorothy Malone	Written on the Wind	TRUE	341
1947	actress	Dorothy McGuire	Gentleman's Agreement	FALSE	342
1981	actor in a leading role	Dudley Moore	Arthur	FALSE	343
1967	actor	Dustin Hoffman	The Graduate	FALSE	344
1969	actor	Dustin Hoffman	Midnight Cowboy	FALSE	345
1974	actor	Dustin Hoffman	Lenny	FALSE	346
1979	actor in a leading role	Dustin Hoffman	Kramer vs. Kramer	TRUE	347
1982	actor in a leading role	Dustin Hoffman	Tootsie	FALSE	348
1988	actor in a leading role	Dustin Hoffman	Rain Man	TRUE	349
1997	actor in a leading role	Dustin Hoffman	Wag the Dog	FALSE	350
1969	actress in a supporting role	Dyan Cannon	Bob & Carol & Ted & Alice	FALSE	351
1978	actress in a supporting role	Dyan Cannon	Heaven Can Wait	FALSE	352
1962	actor in a supporting role	Ed Begley	Sweet Bird of Youth	TRUE	353
1995	actor in a supporting role	Ed Harris	Apollo 13	FALSE	354
1998	actor in a supporting role	Ed Harris	The Truman Show	FALSE	355
2000	actor in a leading role	Ed Harris	Pollock	FALSE	356
2002	actor in a supporting role	Ed Harris	The Hours	FALSE	357
1959	actor in a supporting role	Ed Wynn	The Diary of Anne Frank	FALSE	358
1953	actor in a supporting role	Eddie Albert	Roman Holiday	FALSE	359
1972	actor in a supporting role	Eddie Albert	The Heartbreak Kid	FALSE	360
2006	actor in a supporting role	Eddie Murphy	Dreamgirls	FALSE	361
1954	actor in a supporting role	Edmond O'Brien	The Barefoot Contessa	TRUE	362
1964	actor in a supporting role	Edmond O'Brien	Seven Days in May	FALSE	363
1947	actor in a supporting role	Edmund Gwenn	Miracle on 34th Street	TRUE	364
1950	actor in a supporting role	Edmund Gwenn	Mister 880	FALSE	365
1939	actress in a supporting role	Edna May Oliver	Drums along the Mohawk	FALSE	366
1988	actor in a leading role	Edward James Olmos	Stand and Deliver	FALSE	367
1996	actor in a supporting role	Edward Norton	Primal Fear	FALSE	368
1998	actor in a leading role	Edward Norton	American History X	FALSE	369
1980	actress in a supporting role	Eileen Brennan	Private Benjamin	FALSE	370
1956	actress in a supporting role	Eileen Heckart	The Bad Seed	FALSE	371
1972	actress in a supporting role	Eileen Heckart	Butterflies Are Free	TRUE	372
1950	actress	Eleanor Parker	Caged	FALSE	373
1951	actress	Eleanor Parker	Detective Story	FALSE	374
1955	actress	Eleanor Parker	Interrupted Melody	FALSE	375
1995	actress in a leading role	Elisabeth Shue	Leaving Las Vegas	FALSE	376
1965	actress	Elizabeth Hartman	A Patch of Blue	FALSE	377
1981	actress in a supporting role	Elizabeth McGovern	Ragtime	FALSE	378
1957	actress	Elizabeth Taylor	Raintree County	FALSE	379
1958	actress	Elizabeth Taylor	Cat on a Hot Tin Roof	FALSE	380
1959	actress	Elizabeth Taylor	Suddenly, Last Summer	FALSE	381
1960	actress	Elizabeth Taylor	Butterfield 8	TRUE	382
1966	actress	Elizabeth Taylor	Who's Afraid of Virginia Woolf?	TRUE	383
1971	actress in a supporting role	Ellen Burstyn	The Last Picture Show	FALSE	384
1973	actress	Ellen Burstyn	The Exorcist	FALSE	385
1974	actress	Ellen Burstyn	Alice Doesn't Live Here Anymore	TRUE	386
1978	actress in a leading role	Ellen Burstyn	Same Time, Next Year	FALSE	387
1980	actress in a leading role	Ellen Burstyn	Resurrection	FALSE	388
2000	actress in a leading role	Ellen Burstyn	Requiem for a Dream	FALSE	389
1948	actress in a supporting role	Ellen Corby	I Remember Mama	FALSE	390
2007	actress in a leading role	Ellen Page	Juno	FALSE	391
1969	actor in a supporting role	Elliott Gould	Bob & Carol & Ted & Alice	FALSE	392
1949	actress in a supporting role	Elsa Lanchester	Come to the Stable	FALSE	393
1957	actress in a supporting role	Elsa Lanchester	Witness for the Prosecution	FALSE	394
1996	actress in a leading role	Emily Watson	Breaking the Waves	FALSE	395
1998	actress in a leading role	Emily Watson	Hilary and Jackie	FALSE	396
1992	actress in a leading role	Emma Thompson	Howards End	TRUE	397
1993	actress in a leading role	Emma Thompson	The Remains of the Day	FALSE	398
1993	actress in a supporting role	Emma Thompson	In the Name of the Father	FALSE	399
1995	actress in a leading role	Emma Thompson	Sense and Sensibility	FALSE	400
2012	actress in a leading role	Emmanuelle Riva	Amour	FALSE	401
1985	actor in a supporting role	Eric Roberts	Runaway Train	FALSE	402
1950	actor in a supporting role	Erich von Stroheim	Sunset Blvd.	FALSE	403
1955	actor	Ernest Borgnine	Marty	TRUE	404
1967	actress in a supporting role	Estelle Parsons	Bonnie and Clyde	TRUE	405
1968	actress in a supporting role	Estelle Parsons	Rachel, Rachel	FALSE	406
2001	actor in a supporting role	Ethan Hawke	Training Day	FALSE	407
1944	actress in a supporting role	Ethel Barrymore	None but the Lonely Heart	TRUE	408
1946	actress in a supporting role	Ethel Barrymore	The Spiral Staircase	FALSE	409
1947	actress in a supporting role	Ethel Barrymore	The Paradine Case	FALSE	410
1949	actress in a supporting role	Ethel Barrymore	Pinky	FALSE	411
1949	actress in a supporting role	Ethel Waters	Pinky	FALSE	412
1980	actress in a supporting role	Eva Le Gallienne	Resurrection	FALSE	413
1954	actress in a supporting role	Eva Marie Saint	On the Waterfront	TRUE	414
1945	actress in a supporting role	Eve Arden	Mildred Pierce	FALSE	415
1984	actor in a leading role	F. Murray Abraham	Amadeus	TRUE	416
1938	actress	Fay Bainter	White Banners	FALSE	417
1938	actress in a supporting role	Fay Bainter	Jezebel	TRUE	418
1961	actress in a supporting role	Fay Bainter	The Children's Hour	FALSE	419
1967	actress	Faye Dunaway	Bonnie and Clyde	FALSE	420
1974	actress	Faye Dunaway	Chinatown	FALSE	421
1976	actress in a leading role	Faye Dunaway	Network	TRUE	422
2005	actress in a leading role	Felicity Huffman	Transamerica	FALSE	423
1998	actress in a leading role	Fernanda Montenegro	Central Station	FALSE	424
1946	actress in a supporting role	Flora Robson	Saratoga Trunk	FALSE	425
2006	actor in a leading role	Forest Whitaker	The Last King of Scotland	TRUE	426
1988	actress in a supporting role	Frances McDormand	Mississippi Burning	FALSE	427
1996	actress in a leading role	Frances McDormand	Fargo	TRUE	428
2000	actress in a supporting role	Frances McDormand	Almost Famous	FALSE	429
2005	actress in a supporting role	Frances McDormand	North Country	FALSE	430
1965	actor in a supporting role	Frank Finlay	Othello	FALSE	431
2008	actor in a leading role	Frank Langella	Frost/Nixon	FALSE	432
1942	actor in a supporting role	Frank Morgan	Tortilla Flat	FALSE	433
1953	actor in a supporting role	Frank Sinatra	From Here to Eternity	TRUE	434
1955	actor	Frank Sinatra	The Man with the Golden Arm	FALSE	435
1974	actor in a supporting role	Fred Astaire	The Towering Inferno	FALSE	436
1979	actor in a supporting role	Frederic Forrest	The Rose	FALSE	437
1937	actor	Fredric March	A Star Is Born	FALSE	438
1946	actor	Fredric March	The Best Years of Our Lives	TRUE	439
1951	actor	Fredric March	Death of a Salesman	FALSE	440
2009	actress in a leading role	Gabourey Sidibe	Precious: Based on the Novel 'Push' by Sapphire	FALSE	441
1936	actress in a supporting role	Gale Sondergaard	Anthony Adverse	TRUE	442
1946	actress in a supporting role	Gale Sondergaard	Anna and the King of Siam	FALSE	443
1978	actor in a leading role	Gary Busey	The Buddy Holly Story	FALSE	444
1936	actor	Gary Cooper	Mr. Deeds Goes to Town	FALSE	445
1941	actor	Gary Cooper	Sergeant York	TRUE	446
1942	actor	Gary Cooper	The Pride of the Yankees	FALSE	447
1943	actor	Gary Cooper	For Whom the Bell Tolls	FALSE	448
1952	actor	Gary Cooper	High Noon	TRUE	449
2011	actor in a leading role	Gary Oldman	Tinker Tailor Soldier Spy	FALSE	450
1994	actor in a supporting role	Gary Sinise	Forrest Gump	FALSE	451
1988	actress in a supporting role	Geena Davis	The Accidental Tourist	TRUE	452
1991	actress in a leading role	Geena Davis	Thelma & Louise	FALSE	453
1974	actress	Gena Rowlands	A Woman under the Influence	FALSE	454
1980	actress in a leading role	Gena Rowlands	Gloria	FALSE	455
1967	actor in a supporting role	Gene Hackman	Bonnie and Clyde	FALSE	456
1970	actor in a supporting role	Gene Hackman	I Never Sang for My Father	FALSE	457
1971	actor	Gene Hackman	The French Connection	TRUE	458
1988	actor in a leading role	Gene Hackman	Mississippi Burning	FALSE	459
1992	actor in a supporting role	Gene Hackman	Unforgiven	TRUE	460
1945	actor	Gene Kelly	Anchors Aweigh	FALSE	461
1938	actor in a supporting role	Gene Lockhart	Algiers	FALSE	462
1945	actress	Gene Tierney	Leave Her to Heaven	FALSE	463
1968	actor in a supporting role	Gene Wilder	The Producers	FALSE	464
1969	actress	Genevieve Bujold	Anne of the Thousand Days	FALSE	465
1996	actor in a leading role	Geoffrey Rush	Shine	TRUE	466
1998	actor in a supporting role	Geoffrey Rush	Shakespeare in Love	FALSE	467
2000	actor in a leading role	Geoffrey Rush	Quills	FALSE	468
2010	actor in a supporting role	Geoffrey Rush	The King's Speech	FALSE	469
1975	actor in a supporting role	George Burns	The Sunshine Boys	TRUE	470
1959	actor in a supporting role	George C. Scott	Anatomy of a Murder	FALSE	471
1961	actor in a supporting role	George C. Scott	The Hustler	FALSE	472
1970	actor	George C. Scott	Patton	TRUE	473
1971	actor	George C. Scott	The Hospital	FALSE	474
1961	actor in a supporting role	George Chakiris	West Side Story	TRUE	475
2005	actor in a supporting role	George Clooney	Syriana	TRUE	476
2007	actor in a leading role	George Clooney	Michael Clayton	FALSE	477
2009	actor in a leading role	George Clooney	Up in the Air	FALSE	478
2011	actor in a leading role	George Clooney	The Descendants	FALSE	479
1967	actor in a supporting role	George Kennedy	Cool Hand Luke	TRUE	480
1950	actor in a supporting role	George Sanders	All about Eve	TRUE	481
1966	actor in a supporting role	George Segal	Who's Afraid of Virginia Woolf?	FALSE	482
1939	actress in a supporting role	Geraldine Fitzgerald	Wuthering Heights	FALSE	483
1953	actress in a supporting role	Geraldine Page	Hondo	FALSE	484
1961	actress	Geraldine Page	Summer and Smoke	FALSE	485
1962	actress	Geraldine Page	Sweet Bird of Youth	FALSE	486
1966	actress in a supporting role	Geraldine Page	You're a Big Boy Now	FALSE	487
1972	actress in a supporting role	Geraldine Page	Pete 'n' Tillie	FALSE	488
1978	actress in a leading role	Geraldine Page	Interiors	FALSE	489
1984	actress in a supporting role	Geraldine Page	The Pope of Greenwich Village	FALSE	490
1985	actress in a leading role	Geraldine Page	The Trip to Bountiful	TRUE	491
1990	actor in a leading role	Gerard Depardieu	Cyrano de Bergerac	FALSE	492
1976	actor in a leading role	Giancarlo Giannini	Seven Beauties	FALSE	493
1951	actor in a supporting role	Gig Young	Come Fill the Cup	FALSE	494
1958	actor in a supporting role	Gig Young	Teacher's Pet	FALSE	495
1969	actor in a supporting role	Gig Young	They Shoot Horses, Don't They?	TRUE	496
1940	actress	Ginger Rogers	Kitty Foyle	TRUE	497
1942	actress in a supporting role	Gladys Cooper	Now, Voyager	FALSE	498
1943	actress in a supporting role	Gladys Cooper	The Song of Bernadette	FALSE	499
1964	actress in a supporting role	Gladys Cooper	My Fair Lady	FALSE	500
1936	actress	Gladys George	Valiant Is the Word for Carrie	FALSE	501
1970	actress	Glenda Jackson	Women in Love	TRUE	502
1971	actress	Glenda Jackson	Sunday Bloody Sunday	FALSE	503
1973	actress	Glenda Jackson	A Touch of Class	TRUE	504
1975	actress	Glenda Jackson	Hedda	FALSE	505
1982	actress in a supporting role	Glenn Close	The World According to Garp	FALSE	506
1983	actress in a supporting role	Glenn Close	The Big Chill	FALSE	507
1984	actress in a supporting role	Glenn Close	The Natural	FALSE	508
1987	actress in a leading role	Glenn Close	Fatal Attraction	FALSE	509
1988	actress in a leading role	Glenn Close	Dangerous Liaisons	FALSE	510
2011	actress in a leading role	Glenn Close	Albert Nobbs	FALSE	511
1947	actress in a supporting role	Gloria Grahame	Crossfire	FALSE	512
1952	actress in a supporting role	Gloria Grahame	The Bad and the Beautiful	TRUE	513
1997	actress in a supporting role	Gloria Stuart	Titanic	FALSE	514
1950	actress	Gloria Swanson	Sunset Blvd.	FALSE	515
1960	actress in a supporting role	Glynis Johns	The Sundowners	FALSE	516
1969	actress in a supporting role	Goldie Hawn	Cactus Flower	TRUE	517
1980	actress in a leading role	Goldie Hawn	Private Benjamin	FALSE	518
1953	actress in a supporting role	Grace Kelly	Mogambo	FALSE	519
1954	actress	Grace Kelly	The Country Girl	TRUE	520
1990	actor in a supporting role	Graham Greene	Dances With Wolves	FALSE	521
1964	actress in a supporting role	Grayson Hall	The Night of the Iguana	FALSE	522
1939	actress	Greer Garson	Goodbye, Mr. Chips	FALSE	523
1941	actress	Greer Garson	Blossoms in the Dust	FALSE	524
1942	actress	Greer Garson	Mrs. Miniver	TRUE	525
1943	actress	Greer Garson	Madame Curie	FALSE	526
1944	actress	Greer Garson	Mrs. Parkington	FALSE	527
1945	actress	Greer Garson	The Valley of Decision	FALSE	528
1960	actress	Greer Garson	Sunrise at Campobello	FALSE	529
1997	actor in a supporting role	Greg Kinnear	As Good as It Gets	FALSE	530
1945	actor	Gregory Peck	The Keys of the Kingdom	FALSE	531
1946	actor	Gregory Peck	The Yearling	FALSE	532
1947	actor	Gregory Peck	Gentleman's Agreement	FALSE	533
1949	actor	Gregory Peck	Twelve O'Clock High	FALSE	534
1962	actor	Gregory Peck	To Kill a Mockingbird	TRUE	535
1937	actress	Greta Garbo	Camille	FALSE	536
1939	actress	Greta Garbo	Ninotchka	FALSE	537
1998	actress in a leading role	Gwyneth Paltrow	Shakespeare in Love	TRUE	538
1937	actor in a supporting role	H. B. Warner	Lost Horizon	FALSE	539
2010	actress in a supporting role	Hailee Steinfeld	True Grit	FALSE	540
1984	actor in a supporting role	Haing S. Ngor	The Killing Fields	TRUE	541
2007	actor in a supporting role	Hal Holbrook	Into the Wild	FALSE	542
1999	actor in a supporting role	Haley Joel Osment	The Sixth Sense	FALSE	543
2001	actress in a leading role	Halle Berry	Monster's Ball	TRUE	544
1946	actor in a supporting role	Harold Russell	The Best Years of Our Lives	TRUE	545
1985	actor in a leading role	Harrison Ford	Witness	FALSE	546
1939	actor in a supporting role	Harry Carey	Mr. Smith Goes to Washington	FALSE	547
1991	actor in a supporting role	Harvey Keitel	Bugsy	FALSE	548
1939	actress in a supporting role	Hattie McDaniel	Gone with the Wind	TRUE	549
2005	actor in a leading role	Heath Ledger	Brokeback Mountain	FALSE	550
2008	actor in a supporting role	Heath Ledger	The Dark Knight	TRUE	551
1970	actress in a supporting role	Helen Hayes	Airport	TRUE	552
1997	actress in a leading role	Helen Hunt	As Good as It Gets	TRUE	553
2012	actress in a supporting role	Helen Hunt	The Sessions	FALSE	554
1994	actress in a supporting role	Helen Mirren	The Madness of King George	FALSE	555
2001	actress in a supporting role	Helen Mirren	Gosford Park	FALSE	556
2006	actress in a leading role	Helen Mirren	The Queen	TRUE	557
2009	actress in a leading role	Helen Mirren	The Last Station	FALSE	558
1997	actress in a leading role	Helena Bonham Carter	The Wings of the Dove	FALSE	559
2010	actress in a supporting role	Helena Bonham Carter	The King's Speech	FALSE	560
1940	actor	Henry Fonda	The Grapes of Wrath	FALSE	561
1981	actor in a leading role	Henry Fonda	On Golden Pond	TRUE	562
1942	actor in a supporting role	Henry Travers	Mrs. Miniver	FALSE	563
1959	actress in a supporting role	Hermione Baddeley	Room at the Top	FALSE	564
1999	actress in a leading role	Hilary Swank	Boys Don't Cry	TRUE	565
2004	actress in a leading role	Hilary Swank	Million Dollar Baby	TRUE	566
1987	actress in a leading role	Holly Hunter	Broadcast News	FALSE	567
1993	actress in a leading role	Holly Hunter	The Piano	TRUE	568
1993	actress in a supporting role	Holly Hunter	The Firm	FALSE	569
2003	actress in a supporting role	Holly Hunter	Thirteen	FALSE	570
1950	actress in a supporting role	Hope Emerson	Caged	FALSE	571
1957	actress in a supporting role	Hope Lange	Peyton Place	FALSE	572
1981	actor in a supporting role	Howard E. Rollins, Jr.	Ragtime	FALSE	573
1959	actor in a supporting role	Hugh Griffith	Ben-Hur	TRUE	574
1963	actor in a supporting role	Hugh Griffith	Tom Jones	FALSE	575
2012	actor in a leading role	Hugh Jackman	Les Mis_rables	FALSE	576
1944	actor in a supporting role	Hume Cronyn	The Seventh Cross	FALSE	577
1943	actor	Humphrey Bogart	Casablanca	FALSE	578
1951	actor	Humphrey Bogart	The African Queen	TRUE	579
1954	actor	Humphrey Bogart	The Caine Mutiny	FALSE	580
1965	actor in a supporting role	Ian Bannen	The Flight of the Phoenix	FALSE	581
1981	actor in a supporting role	Ian Holm	Chariots of Fire	FALSE	582
1998	actor in a leading role	Ian McKellen	Gods and Monsters	FALSE	583
2001	actor in a supporting role	Ian McKellen	The Lord of the Rings: The Fellowship of the Ring	FALSE	584
1966	actress	Ida Kaminska	The Shop on Main Street	FALSE	585
2004	actress in a leading role	Imelda Staunton	Vera Drake	FALSE	586
1943	actress	Ingrid Bergman	For Whom the Bell Tolls	FALSE	587
1944	actress	Ingrid Bergman	Gaslight	TRUE	588
1945	actress	Ingrid Bergman	The Bells of St. Mary's	FALSE	589
1948	actress	Ingrid Bergman	Joan of Arc	FALSE	590
1956	actress	Ingrid Bergman	Anastasia	TRUE	591
1974	actress in a supporting role	Ingrid Bergman	Murder on the Orient Express	TRUE	592
1978	actress in a leading role	Ingrid Bergman	Autumn Sonata	FALSE	593
1936	actress	Irene Dunne	Theodora Goes Wild	FALSE	594
1937	actress	Irene Dunne	The Awful Truth	FALSE	595
1939	actress	Irene Dunne	Love Affair	FALSE	596
1948	actress	Irene Dunne	I Remember Mama	FALSE	597
1975	actress	Isabelle Adjani	The Story of Adele H.	FALSE	598
1989	actress in a leading role	Isabelle Adjani	Camille Claudel	FALSE	599
1943	actor in a supporting role	J. Carrol Naish	Sahara	FALSE	600
1945	actor in a supporting role	J. Carrol Naish	A Medal for Benny	FALSE	601
1968	actor in a supporting role	Jack Albertson	The Subject Was Roses	TRUE	602
1973	actor in a supporting role	Jack Gilford	Save the Tiger	FALSE	603
1960	actor in a supporting role	Jack Kruschen	The Apartment	FALSE	604
1955	actor in a supporting role	Jack Lemmon	Mister Roberts	TRUE	605
1959	actor	Jack Lemmon	Some Like It Hot	FALSE	606
1960	actor	Jack Lemmon	The Apartment	FALSE	607
1962	actor	Jack Lemmon	Days of Wine and Roses	FALSE	608
1973	actor	Jack Lemmon	Save the Tiger	TRUE	609
1979	actor in a leading role	Jack Lemmon	The China Syndrome	FALSE	610
1980	actor in a leading role	Jack Lemmon	Tribute	FALSE	611
1982	actor in a leading role	Jack Lemmon	Missing	FALSE	612
1969	actor in a supporting role	Jack Nicholson	Easy Rider	FALSE	613
1970	actor	Jack Nicholson	Five Easy Pieces	FALSE	614
1973	actor	Jack Nicholson	The Last Detail	FALSE	615
1974	actor	Jack Nicholson	Chinatown	FALSE	616
1975	actor	Jack Nicholson	One Flew over the Cuckoo's Nest	TRUE	617
1981	actor in a supporting role	Jack Nicholson	Reds	FALSE	618
1983	actor in a supporting role	Jack Nicholson	Terms of Endearment	TRUE	619
1985	actor in a leading role	Jack Nicholson	Prizzi's Honor	FALSE	620
1987	actor in a leading role	Jack Nicholson	Ironweed	FALSE	621
1992	actor in a supporting role	Jack Nicholson	A Few Good Men	FALSE	622
1997	actor in a leading role	Jack Nicholson	As Good as It Gets	TRUE	623
2002	actor in a leading role	Jack Nicholson	About Schmidt	FALSE	624
1940	actor in a supporting role	Jack Oakie	The Great Dictator	FALSE	625
1952	actor in a supporting role	Jack Palance	Sudden Fear	FALSE	626
1953	actor in a supporting role	Jack Palance	Shane	FALSE	627
1991	actor in a supporting role	Jack Palance	City Slickers	TRUE	628
1975	actor in a supporting role	Jack Warden	Shampoo	FALSE	629
1978	actor in a supporting role	Jack Warden	Heaven Can Wait	FALSE	630
1968	actor in a supporting role	Jack Wild	Oliver!	FALSE	631
2010	actress in a supporting role	Jacki Weaver	Animal Kingdom	FALSE	632
2012	actress in a supporting role	Jacki Weaver	Silver Linings Playbook	FALSE	633
2006	actor in a supporting role	Jackie Earle Haley	Little Children	FALSE	634
1961	actor in a supporting role	Jackie Gleason	The Hustler	FALSE	635
2005	actor in a supporting role	Jake Gyllenhaal	Brokeback Mountain	FALSE	636
1972	actor in a supporting role	James Caan	The Godfather	FALSE	637
1938	actor	James Cagney	Angels with Dirty Faces	FALSE	638
1942	actor	James Cagney	Yankee Doodle Dandy	TRUE	639
1955	actor	James Cagney	Love Me or Leave Me	FALSE	640
1998	actor in a supporting role	James Coburn	Affliction	TRUE	641
1981	actor in a supporting role	James Coco	Only When I Laugh	FALSE	642
1995	actor in a supporting role	James Cromwell	Babe	FALSE	643
1955	actor	James Dean	East of Eden	FALSE	644
1956	actor	James Dean	Giant	FALSE	645
1945	actor in a supporting role	James Dunn	A Tree Grows in Brooklyn	TRUE	646
1970	actor	James Earl Jones	The Great White Hope	FALSE	647
2010	actor in a leading role	James Franco	127 Hours	FALSE	648
1985	actor in a leading role	James Garner	Murphy's Romance	FALSE	649
1941	actor in a supporting role	James Gleason	Here Comes Mr. Jordan	FALSE	650
1954	actor	James Mason	A Star Is Born	FALSE	651
1966	actor in a supporting role	James Mason	Georgy Girl	FALSE	652
1982	actor in a supporting role	James Mason	The Verdict	FALSE	653
1940	actor in a supporting role	James Stephenson	The Letter	FALSE	654
1939	actor	James Stewart	Mr. Smith Goes to Washington	FALSE	655
1940	actor	James Stewart	The Philadelphia Story	TRUE	656
1946	actor	James Stewart	It's a Wonderful Life	FALSE	657
1950	actor	James Stewart	Harvey	FALSE	658
1959	actor	James Stewart	Anatomy of a Murder	FALSE	659
1949	actor in a supporting role	James Whitmore	Battleground	FALSE	660
1975	actor	James Whitmore	Give 'em Hell, Harry!	FALSE	661
1986	actor in a leading role	James Woods	Salvador	FALSE	662
1996	actor in a supporting role	James Woods	Ghosts of Mississippi	FALSE	663
2004	actor in a leading role	Jamie Foxx	Ray	TRUE	664
2004	actor in a supporting role	Jamie Foxx	Collateral	FALSE	665
1954	actress in a supporting role	Jan Sterling	The High and the Mighty	FALSE	666
1970	actress	Jane Alexander	The Great White Hope	FALSE	667
1976	actress in a supporting role	Jane Alexander	All the President's Men	FALSE	668
1979	actress in a supporting role	Jane Alexander	Kramer vs. Kramer	FALSE	669
1983	actress in a leading role	Jane Alexander	Testament	FALSE	670
1940	actress in a supporting role	Jane Darwell	The Grapes of Wrath	TRUE	671
1969	actress	Jane Fonda	They Shoot Horses, Don't They?	FALSE	672
1971	actress	Jane Fonda	Klute	TRUE	673
1977	actress in a leading role	Jane Fonda	Julia	FALSE	674
1978	actress in a leading role	Jane Fonda	Coming Home	TRUE	675
1979	actress in a leading role	Jane Fonda	The China Syndrome	FALSE	676
1981	actress in a supporting role	Jane Fonda	On Golden Pond	FALSE	677
1986	actress in a leading role	Jane Fonda	The Morning After	FALSE	678
1946	actress	Jane Wyman	The Yearling	FALSE	679
1948	actress	Jane Wyman	Johnny Belinda	TRUE	680
1951	actress	Jane Wyman	The Blue Veil	FALSE	681
1954	actress	Jane Wyman	Magnificent Obsession	FALSE	682
1937	actress	Janet Gaynor	A Star Is Born	FALSE	683
1960	actress in a supporting role	Janet Leigh	Psycho	FALSE	684
1999	actress in a leading role	Janet McTeer	Tumbleweeds	FALSE	685
2011	actress in a supporting role	Janet McTeer	Albert Nobbs	FALSE	686
1971	actress	Janet Suzman	Nicholas and Alexandra	FALSE	687
1973	actor in a supporting role	Jason Miller	The Exorcist	FALSE	688
1976	actor in a supporting role	Jason Robards	All the President's Men	TRUE	689
1977	actor in a supporting role	Jason Robards	Julia	TRUE	690
1980	actor in a supporting role	Jason Robards	Melvin and Howard	FALSE	691
2000	actor in a leading role	Javier Bardem	Before Night Falls	FALSE	692
2007	actor in a supporting role	Javier Bardem	No Country for Old Men	TRUE	693
2010	actor in a leading role	Javier Bardem	Biutiful	FALSE	694
1992	actor in a supporting role	Jaye Davidson	The Crying Game	FALSE	695
1943	actress	Jean Arthur	The More the Merrier	FALSE	696
2011	actor in a leading role	Jean Dujardin	The Artist	TRUE	697
1952	actress in a supporting role	Jean Hagen	Singin' in the Rain	FALSE	698
1948	actress in a supporting role	Jean Simmons	Hamlet	FALSE	699
1969	actress	Jean Simmons	The Happy Ending	FALSE	700
1949	actress	Jeanne Crain	Pinky	FALSE	701
1972	actress in a supporting role	Jeannie Berlin	The Heartbreak Kid	FALSE	702
1971	actor in a supporting role	Jeff Bridges	The Last Picture Show	FALSE	703
1974	actor in a supporting role	Jeff Bridges	Thunderbolt and Lightfoot	FALSE	704
1984	actor in a leading role	Jeff Bridges	Starman	FALSE	705
2000	actor in a supporting role	Jeff Bridges	The Contender	FALSE	706
2009	actor in a leading role	Jeff Bridges	Crazy Heart	TRUE	707
2010	actor in a leading role	Jeff Bridges	True Grit	FALSE	708
1950	actor in a supporting role	Jeff Chandler	Broken Arrow	FALSE	709
2001	actress in a supporting role	Jennifer Connelly	A Beautiful Mind	TRUE	710
2006	actress in a supporting role	Jennifer Hudson	Dreamgirls	TRUE	711
1943	actress	Jennifer Jones	The Song of Bernadette	TRUE	712
1944	actress in a supporting role	Jennifer Jones	Since You Went Away	FALSE	713
1945	actress	Jennifer Jones	Love Letters	FALSE	714
1946	actress	Jennifer Jones	Duel in the Sun	FALSE	715
1955	actress	Jennifer Jones	Love Is a Many-Splendored Thing	FALSE	716
2010	actress in a leading role	Jennifer Lawrence	Winter's Bone	FALSE	717
2012	actress in a leading role	Jennifer Lawrence	Silver Linings Playbook	TRUE	718
1994	actress in a supporting role	Jennifer Tilly	Bullets over Broadway	FALSE	719
1990	actor in a leading role	Jeremy Irons	Reversal of Fortune	TRUE	720
2009	actor in a leading role	Jeremy Renner	The Hurt Locker	FALSE	721
2010	actor in a supporting role	Jeremy Renner	The Town	FALSE	722
2010	actor in a leading role	Jesse Eisenberg	The Social Network	FALSE	723
2011	actress in a supporting role	Jessica Chastain	The Help	FALSE	724
2012	actress in a leading role	Jessica Chastain	Zero Dark Thirty	FALSE	725
1982	actress in a leading role	Jessica Lange	Frances	FALSE	726
1982	actress in a supporting role	Jessica Lange	Tootsie	TRUE	727
1984	actress in a leading role	Jessica Lange	Country	FALSE	728
1985	actress in a leading role	Jessica Lange	Sweet Dreams	FALSE	729
1989	actress in a leading role	Jessica Lange	Music Box	FALSE	730
1994	actress in a leading role	Jessica Lange	Blue Sky	TRUE	731
1989	actress in a leading role	Jessica Tandy	Driving Miss Daisy	TRUE	732
1991	actress in a supporting role	Jessica Tandy	Fried Green Tomatoes	FALSE	733
1978	actress in a leading role	Jill Clayburgh	An Unmarried Woman	FALSE	734
1979	actress in a leading role	Jill Clayburgh	Starting Over	FALSE	735
2001	actor in a supporting role	Jim Broadbent	Iris	TRUE	736
1955	actress in a supporting role	Jo Van Fleet	East of Eden	TRUE	737
1995	actress in a supporting role	Joan Allen	Nixon	FALSE	738
1996	actress in a supporting role	Joan Allen	The Crucible	FALSE	739
2000	actress in a leading role	Joan Allen	The Contender	FALSE	740
1951	actress in a supporting role	Joan Blondell	The Blue Veil	FALSE	741
1945	actress	Joan Crawford	Mildred Pierce	TRUE	742
1947	actress	Joan Crawford	Possessed	FALSE	743
1952	actress	Joan Crawford	Sudden Fear	FALSE	744
1988	actress in a supporting role	Joan Cusack	Working Girl	FALSE	745
1997	actress in a supporting role	Joan Cusack	In & Out	FALSE	746
1940	actress	Joan Fontaine	Rebecca	FALSE	747
1941	actress	Joan Fontaine	Suspicion	TRUE	748
1943	actress	Joan Fontaine	The Constant Nymph	FALSE	749
1981	actress in a supporting role	Joan Hackett	Only When I Laugh	FALSE	750
1945	actress in a supporting role	Joan Lorring	The Corn Is Green	FALSE	751
1992	actress in a supporting role	Joan Plowright	Enchanted April	FALSE	752
1957	actress	Joanne Woodward	The Three Faces of Eve	TRUE	753
1968	actress	Joanne Woodward	Rachel, Rachel	FALSE	754
1973	actress	Joanne Woodward	Summer Wishes, Winter Dreams	FALSE	755
1990	actress in a leading role	Joanne Woodward	Mr. & Mrs. Bridge	FALSE	756
2000	actor in a supporting role	Joaquin Phoenix	Gladiator	FALSE	757
2005	actor in a leading role	Joaquin Phoenix	Walk the Line	FALSE	758
2012	actor in a leading role	Joaquin Phoenix	The Master	FALSE	759
1966	actress in a supporting role	Jocelyne Lagarde	Hawaii	FALSE	760
1976	actress in a supporting role	Jodie Foster	Taxi Driver	FALSE	761
1988	actress in a leading role	Jodie Foster	The Accused	TRUE	762
1991	actress in a leading role	Jodie Foster	The Silence of the Lambs	TRUE	763
1994	actress in a leading role	Jodie Foster	Nell	FALSE	764
1955	actor in a supporting role	Joe Mantell	Marty	FALSE	765
1980	actor in a supporting role	Joe Pesci	Raging Bull	FALSE	766
1990	actor in a supporting role	Joe Pesci	Good Fellas	TRUE	767
1972	actor in a supporting role	Joel Grey	Cabaret	TRUE	768
2002	actor in a supporting role	John C. Reilly	Chicago	FALSE	769
1967	actor in a supporting role	John Cassavetes	The Dirty Dozen	FALSE	770
1945	actor in a supporting role	John Dall	The Corn Is Green	FALSE	771
1938	actor in a supporting role	John Garfield	Four Daughters	FALSE	772
1947	actor	John Garfield	Body and Soul	FALSE	773
1964	actor in a supporting role	John Gielgud	Becket	FALSE	774
1981	actor in a supporting role	John Gielgud	Arthur	TRUE	775
2010	actor in a supporting role	John Hawkes	Winter's Bone	FALSE	776
1973	actor in a supporting role	John Houseman	The Paper Chase	TRUE	777
1978	actor in a supporting role	John Hurt	Midnight Express	FALSE	778
1980	actor in a leading role	John Hurt	The Elephant Man	FALSE	779
1963	actor in a supporting role	John Huston	The Cardinal	FALSE	780
1949	actor in a supporting role	John Ireland	All the King's Men	FALSE	781
1982	actor in a supporting role	John Lithgow	The World According to Garp	FALSE	782
1983	actor in a supporting role	John Lithgow	Terms of Endearment	FALSE	783
1984	actor in a supporting role	John Malkovich	Places in the Heart	FALSE	784
1993	actor in a supporting role	John Malkovich	In the Line of Fire	FALSE	785
1970	actor in a supporting role	John Marley	Love Story	FALSE	786
1970	actor in a supporting role	John Mills	Ryan's Daughter	TRUE	787
1977	actor in a leading role	John Travolta	Saturday Night Fever	FALSE	788
1994	actor in a leading role	John Travolta	Pulp Fiction	FALSE	789
1949	actor	John Wayne	Sands of Iwo Jima	FALSE	790
1969	actor	John Wayne	True Grit	TRUE	791
2003	actor in a leading role	Johnny Depp	Pirates of the Caribbean: The Curse of the Black Pearl	FALSE	792
2004	actor in a leading role	Johnny Depp	Finding Neverland	FALSE	793
2007	actor in a leading role	Johnny Depp	Sweeney Todd The Demon Barber of Fleet Street	FALSE	794
1969	actor	Jon Voight	Midnight Cowboy	FALSE	795
1978	actor in a leading role	Jon Voight	Coming Home	TRUE	796
1985	actor in a leading role	Jon Voight	Runaway Train	FALSE	797
2001	actor in a supporting role	Jon Voight	Ali	FALSE	798
2011	actor in a supporting role	Jonah Hill	Moneyball	FALSE	799
1948	actor in a supporting role	Jos_ Ferrer	Joan of Arc	FALSE	800
1950	actor	Jos_ Ferrer	Cyrano de Bergerac	TRUE	801
1952	actor	Jos_ Ferrer	Moulin Rouge	FALSE	802
1937	actor in a supporting role	Joseph Schildkraut	The Life of Emile Zola	TRUE	803
1950	actress in a supporting role	Josephine Hull	Harvey	TRUE	804
2008	actor in a supporting role	Josh Brolin	Milk	FALSE	805
1963	actress in a supporting role	Joyce Redman	Tom Jones	FALSE	806
1965	actress in a supporting role	Joyce Redman	Othello	FALSE	807
1959	actress in a supporting role	Juanita Moore	Imitation of Life	FALSE	808
1980	actor in a supporting role	Judd Hirsch	Ordinary People	FALSE	809
1999	actor in a supporting role	Jude Law	The Talented Mr. Ripley	FALSE	810
2003	actor in a leading role	Jude Law	Cold Mountain	FALSE	811
1997	actress in a leading role	Judi Dench	Mrs. Brown	FALSE	812
1998	actress in a supporting role	Judi Dench	Shakespeare in Love	TRUE	813
2000	actress in a supporting role	Judi Dench	Chocolat	FALSE	814
2001	actress in a leading role	Judi Dench	Iris	FALSE	815
2005	actress in a leading role	Judi Dench	Mrs. Henderson Presents	FALSE	816
2006	actress in a leading role	Judi Dench	Notes on a Scandal	FALSE	817
1940	actress in a supporting role	Judith Anderson	Rebecca	FALSE	818
1984	actress in a leading role	Judy Davis	A Passage to India	FALSE	819
1992	actress in a supporting role	Judy Davis	Husbands and Wives	FALSE	820
1954	actress	Judy Garland	A Star Is Born	FALSE	821
1961	actress in a supporting role	Judy Garland	Judgment at Nuremberg	FALSE	822
1950	actress	Judy Holliday	Born Yesterday	TRUE	823
1989	actress in a supporting role	Julia Roberts	Steel Magnolias	FALSE	824
1990	actress in a leading role	Julia Roberts	Pretty Woman	FALSE	825
2000	actress in a leading role	Julia Roberts	Erin Brockovich	TRUE	826
1997	actress in a supporting role	Julianne Moore	Boogie Nights	FALSE	827
1999	actress in a leading role	Julianne Moore	The End of the Affair	FALSE	828
2002	actress in a leading role	Julianne Moore	Far from Heaven	FALSE	829
2002	actress in a supporting role	Julianne Moore	The Hours	FALSE	830
1964	actress	Julie Andrews	Mary Poppins	TRUE	831
1965	actress	Julie Andrews	The Sound of Music	FALSE	832
1982	actress in a leading role	Julie Andrews	Victor/Victoria	FALSE	833
1965	actress	Julie Christie	Darling	TRUE	834
1971	actress	Julie Christie	McCabe & Mrs. Miller	FALSE	835
1997	actress in a leading role	Julie Christie	Afterglow	FALSE	836
2007	actress in a leading role	Julie Christie	Away from Her	FALSE	837
1952	actress	Julie Harris	The Member of the Wedding	FALSE	838
1983	actress in a leading role	Julie Walters	Educating Rita	FALSE	839
2000	actress in a supporting role	Julie Walters	Billy Elliot	FALSE	840
1996	actress in a supporting role	Juliette Binoche	The English Patient	TRUE	841
2000	actress in a leading role	Juliette Binoche	Chocolat	FALSE	842
1991	actress in a supporting role	Juliette Lewis	Cape Fear	FALSE	843
1979	actor in a supporting role	Justin Henry	Kramer vs. Kramer	FALSE	844
1970	actress in a supporting role	Karen Black	Five Easy Pieces	FALSE	845
1951	actor in a supporting role	Karl Malden	A Streetcar Named Desire	TRUE	846
1954	actor in a supporting role	Karl Malden	On the Waterfront	FALSE	847
2000	actress in a supporting role	Kate Hudson	Almost Famous	FALSE	848
1991	actress in a supporting role	Kate Nelligan	The Prince of Tides	FALSE	849
1995	actress in a supporting role	Kate Winslet	Sense and Sensibility	FALSE	850
1997	actress in a leading role	Kate Winslet	Titanic	FALSE	851
2001	actress in a supporting role	Kate Winslet	Iris	FALSE	852
2004	actress in a leading role	Kate Winslet	Eternal Sunshine of the Spotless Mind	FALSE	853
2006	actress in a leading role	Kate Winslet	Little Children	FALSE	854
2008	actress in a leading role	Kate Winslet	The Reader	TRUE	855
1940	actress	Katharine Hepburn	The Philadelphia Story	FALSE	856
1942	actress	Katharine Hepburn	Woman of the Year	FALSE	857
1951	actress	Katharine Hepburn	The African Queen	FALSE	858
1955	actress	Katharine Hepburn	Summertime	FALSE	859
1956	actress	Katharine Hepburn	The Rainmaker	FALSE	860
1959	actress	Katharine Hepburn	Suddenly, Last Summer	FALSE	861
1962	actress	Katharine Hepburn	Long Day's Journey into Night	FALSE	862
1967	actress	Katharine Hepburn	Guess Who's Coming to Dinner	TRUE	863
1968	actress	Katharine Hepburn	The Lion in Winter	TRUE	864
1981	actress in a leading role	Katharine Hepburn	On Golden Pond	TRUE	865
1967	actress in a supporting role	Katharine Ross	The Graduate	FALSE	866
1995	actress in a supporting role	Kathleen Quinlan	Apollo 13	FALSE	867
1986	actress in a leading role	Kathleen Turner	Peggy Sue Got Married	FALSE	868
1990	actress in a leading role	Kathy Bates	Misery	TRUE	869
1998	actress in a supporting role	Kathy Bates	Primary Colors	FALSE	870
2002	actress in a supporting role	Kathy Bates	About Schmidt	FALSE	871
1943	actress in a supporting role	Katina Paxinou	For Whom the Bell Tolls	TRUE	872
1954	actress in a supporting role	Katy Jurado	Broken Lance	FALSE	873
1968	actress in a supporting role	Kay Medford	Funny Girl	FALSE	874
2005	actress in a leading role	Keira Knightley	Pride & Prejudice	FALSE	875
2003	actress in a leading role	Keisha Castle-Hughes	Whale Rider	FALSE	876
2003	actor in a supporting role	Ken Watanabe	The Last Samurai	FALSE	877
1989	actor in a leading role	Kenneth Branagh	Henry V	FALSE	878
2011	actor in a supporting role	Kenneth Branagh	My Week with Marilyn	FALSE	879
1990	actor in a leading role	Kevin Costner	Dances With Wolves	FALSE	880
1988	actor in a supporting role	Kevin Kline	A Fish Called Wanda	TRUE	881
1951	actor in a supporting role	Kevin McCarthy	Death of a Salesman	FALSE	882
1995	actor in a supporting role	Kevin Spacey	The Usual Suspects	TRUE	883
1999	actor in a leading role	Kevin Spacey	American Beauty	TRUE	884
1997	actress in a supporting role	Kim Basinger	L.A. Confidential	TRUE	885
1951	actress in a supporting role	Kim Hunter	A Streetcar Named Desire	TRUE	886
1964	actress	Kim Stanley	Seance on a Wet Afternoon	FALSE	887
1982	actress in a supporting role	Kim Stanley	Frances	FALSE	888
1949	actor	Kirk Douglas	Champion	FALSE	889
1952	actor	Kirk Douglas	The Bad and the Beautiful	FALSE	890
1956	actor	Kirk Douglas	Lust for Life	FALSE	891
1985	actor in a supporting role	Klaus Maria Brandauer	Out of Africa	FALSE	892
1996	actress in a leading role	Kristin Scott Thomas	The English Patient	FALSE	893
1957	actress	Lana Turner	Peyton Place	FALSE	894
1946	actor	Larry Parks	The Jolson Story	FALSE	895
1991	actress in a leading role	Laura Dern	Rambling Rose	FALSE	896
2000	actress in a leading role	Laura Linney	You Can Count on Me	FALSE	897
2004	actress in a supporting role	Laura Linney	Kinsey	FALSE	898
2007	actress in a leading role	Laura Linney	The Savages	FALSE	899
1996	actress in a supporting role	Lauren Bacall	The Mirror Has Two Faces	FALSE	900
1993	actor in a leading role	Laurence Fishburne	What's Love Got to Do with It	FALSE	901
1959	actor	Laurence Harvey	Room at the Top	FALSE	902
1939	actor	Laurence Olivier	Wuthering Heights	FALSE	903
1940	actor	Laurence Olivier	Rebecca	FALSE	904
1946	actor	Laurence Olivier	Henry V	FALSE	905
1948	actor	Laurence Olivier	Hamlet	TRUE	906
1960	actor	Laurence Olivier	The Entertainer	FALSE	907
1965	actor	Laurence Olivier	Othello	FALSE	908
1972	actor	Laurence Olivier	Sleuth	FALSE	909
1976	actor in a supporting role	Laurence Olivier	Marathon Man	FALSE	910
1978	actor in a leading role	Laurence Olivier	The Boys from Brazil	FALSE	911
1951	actress in a supporting role	Lee Grant	Detective Story	FALSE	912
1970	actress in a supporting role	Lee Grant	The Landlord	FALSE	913
1975	actress in a supporting role	Lee Grant	Shampoo	TRUE	914
1976	actress in a supporting role	Lee Grant	Voyage of the Damned	FALSE	915
1954	actor in a supporting role	Lee J. Cobb	On the Waterfront	FALSE	916
1958	actor in a supporting role	Lee J. Cobb	The Brothers Karamazov	FALSE	917
1965	actor	Lee Marvin	Cat Ballou	TRUE	918
1962	actress	Lee Remick	Days of Wine and Roses	FALSE	919
1974	actor in a supporting role	Lee Strasberg	The Godfather Part II	FALSE	920
1964	actor in a supporting role	Lee Tracy	The Best Man	FALSE	921
1989	actress in a supporting role	Lena Olin	Enemies, A Love Story	FALSE	922
1951	actor in a supporting role	Leo Genn	Quo Vadis	FALSE	923
1971	actor in a supporting role	Leonard Frey	Fiddler on the Roof	FALSE	924
1993	actor in a supporting role	Leonardo DiCaprio	What's Eating Gilbert Grape	FALSE	925
2004	actor in a leading role	Leonardo DiCaprio	The Aviator	FALSE	926
2006	actor in a leading role	Leonardo DiCaprio	Blood Diamond	FALSE	927
1982	actress in a supporting role	Lesley Ann Warren	Victor/Victoria	FALSE	928
1977	actress in a supporting role	Leslie Browne	The Turning Point	FALSE	929
1953	actress	Leslie Caron	Lili	FALSE	930
1963	actress	Leslie Caron	The L-Shaped Room	FALSE	931
1938	actor	Leslie Howard	Pygmalion	FALSE	932
1948	actor	Lew Ayres	Johnny Belinda	FALSE	933
1993	actor in a leading role	Liam Neeson	Schindler's List	FALSE	934
1964	actress in a supporting role	Lila Kedrova	Zorba the Greek	TRUE	935
1963	actress in a supporting role	Lilia Skala	Lilies of the Field	FALSE	936
1946	actress in a supporting role	Lillian Gish	Duel in the Sun	FALSE	937
1975	actress in a supporting role	Lily Tomlin	Nashville	FALSE	938
1973	actress in a supporting role	Linda Blair	The Exorcist	FALSE	939
1983	actress in a supporting role	Linda Hunt	The Year of Living Dangerously	TRUE	940
1984	actress in a supporting role	Lindsay Crouse	Places in the Heart	FALSE	941
1972	actress	Liv Ullmann	The Emigrants	FALSE	942
1976	actress in a leading role	Liv Ullmann	Face to Face	FALSE	943
1969	actress	Liza Minnelli	The Sterile Cuckoo	FALSE	944
1972	actress	Liza Minnelli	Cabaret	TRUE	945
1947	actress	Loretta Young	The Farmer's Daughter	TRUE	946
1949	actress	Loretta Young	Come to the Stable	FALSE	947
1990	actress in a supporting role	Lorraine Bracco	Good Fellas	FALSE	948
1961	actress in a supporting role	Lotte Lenya	The Roman Spring of Mrs. Stone	FALSE	949
1950	actor	Louis Calhern	The Magnificent Yankee	FALSE	950
1982	actor in a supporting role	Louis Gossett, Jr.	An Officer and a Gentleman	TRUE	951
1975	actress	Louise Fletcher	One Flew over the Cuckoo's Nest	TRUE	952
1943	actress in a supporting role	Lucile Watson	Watch on the Rhine	FALSE	953
1936	actress	Luise Rainer	The Great Ziegfeld	TRUE	954
1937	actress	Luise Rainer	The Good Earth	TRUE	955
1968	actress in a supporting role	Lynn Carlin	Faces	FALSE	956
1966	actress	Lynn Redgrave	Georgy Girl	FALSE	957
1998	actress in a supporting role	Lynn Redgrave	Gods and Monsters	FALSE	958
1973	actress in a supporting role	Madeline Kahn	Paper Moon	FALSE	959
1974	actress in a supporting role	Madeline Kahn	Blazing Saddles	FALSE	960
2009	actress in a supporting role	Maggie Gyllenhaal	Crazy Heart	FALSE	961
1953	actress	Maggie McNamara	The Moon Is Blue	FALSE	962
1965	actress in a supporting role	Maggie Smith	Othello	FALSE	963
1969	actress	Maggie Smith	The Prime of Miss Jean Brodie	TRUE	964
1972	actress	Maggie Smith	Travels with My Aunt	FALSE	965
1978	actress in a supporting role	Maggie Smith	California Suite	TRUE	966
1986	actress in a supporting role	Maggie Smith	A Room with a View	FALSE	967
2001	actress in a supporting role	Maggie Smith	Gosford Park	FALSE	968
1966	actor in a supporting role	Mako	The Sand Pebbles	FALSE	969
1962	actor	Marcello Mastroianni	Divorce--Italian Style	FALSE	970
1977	actor in a leading role	Marcello Mastroianni	A Special Day	FALSE	971
1987	actor in a leading role	Marcello Mastroianni	Dark Eyes	FALSE	972
2000	actress in a supporting role	Marcia Gay Harden	Pollock	TRUE	973
2003	actress in a supporting role	Marcia Gay Harden	Mystic River	FALSE	974
1995	actress in a supporting role	Mare Winningham	Georgia	FALSE	975
1985	actress in a supporting role	Margaret Avery	The Color Purple	FALSE	976
1971	actress in a supporting role	Margaret Leighton	The Go-Between	FALSE	977
1963	actress in a supporting role	Margaret Rutherford	The V.I.P.s	TRUE	978
1938	actress	Margaret Sullavan	Three Comrades	FALSE	979
1941	actress in a supporting role	Margaret Wycherly	Sergeant York	FALSE	980
1936	actress in a supporting role	Maria Ouspenskaya	Dodsworth	FALSE	981
1939	actress in a supporting role	Maria Ouspenskaya	Love Affair	FALSE	982
1996	actress in a supporting role	Marianne Jean-Baptiste	Secrets & Lies	FALSE	983
1976	actress in a leading role	Marie-Christine Barrault	Cousin, Cousine	FALSE	984
1979	actress in a supporting role	Mariel Hemingway	Manhattan	FALSE	985
2007	actress in a leading role	Marion Cotillard	La Vie en Rose	TRUE	986
1955	actress in a supporting role	Marisa Pavan	The Rose Tattoo	FALSE	987
1992	actress in a supporting role	Marisa Tomei	My Cousin Vinny	TRUE	988
2001	actress in a supporting role	Marisa Tomei	In the Bedroom	FALSE	989
2008	actress in a supporting role	Marisa Tomei	The Wrestler	FALSE	990
1947	actress in a supporting role	Marjorie Main	The Egg and I	FALSE	991
1940	actress in a supporting role	Marjorie Rambeau	Primrose Path	FALSE	992
1953	actress in a supporting role	Marjorie Rambeau	Torch Song	FALSE	993
2010	actor in a supporting role	Mark Ruffalo	The Kids Are All Right	FALSE	994
2006	actor in a supporting role	Mark Wahlberg	The Departed	FALSE	995
1986	actress in a leading role	Marlee Matlin	Children of a Lesser God	TRUE	996
1951	actor	Marlon Brando	A Streetcar Named Desire	FALSE	997
1952	actor	Marlon Brando	Viva Zapata!	FALSE	998
1953	actor	Marlon Brando	Julius Caesar	FALSE	999
1954	actor	Marlon Brando	On the Waterfront	TRUE	1000
1957	actor	Marlon Brando	Sayonara	FALSE	1001
1972	actor	Marlon Brando	The Godfather	TRUE	1002
1973	actor	Marlon Brando	Last Tango in Paris	FALSE	1003
1989	actor in a supporting role	Marlon Brando	A Dry White Season	FALSE	1004
1973	actress	Marsha Mason	Cinderella Liberty	FALSE	1005
1977	actress in a leading role	Marsha Mason	The Goodbye Girl	FALSE	1006
1979	actress in a leading role	Marsha Mason	Chapter Two	FALSE	1007
1981	actress in a leading role	Marsha Mason	Only When I Laugh	FALSE	1008
1958	actress in a supporting role	Martha Hyer	Some Came Running	FALSE	1009
1940	actress	Martha Scott	Our Town	FALSE	1010
1965	actor in a supporting role	Martin Balsam	A Thousand Clowns	TRUE	1011
1988	actor in a supporting role	Martin Landau	Tucker The Man and His Dream	FALSE	1012
1989	actor in a supporting role	Martin Landau	Crimes and Misdemeanors	FALSE	1013
1994	actor in a supporting role	Martin Landau	Ed Wood	TRUE	1014
1941	actress in a supporting role	Mary Astor	The Great Lie	TRUE	1015
1962	actress in a supporting role	Mary Badham	To Kill a Mockingbird	FALSE	1016
1986	actress in a supporting role	Mary Elizabeth Mastrantonio	The Color of Money	FALSE	1017
1990	actress in a supporting role	Mary McDonnell	Dances With Wolves	FALSE	1018
1992	actress in a leading role	Mary McDonnell	Passion Fish	FALSE	1019
1980	actress in a supporting role	Mary Steenburgen	Melvin and Howard	TRUE	1020
1980	actress in a leading role	Mary Tyler Moore	Ordinary People	FALSE	1021
1960	actress in a supporting role	Mary Ure	Sons and Lovers	FALSE	1022
1995	actor in a leading role	Massimo Troisi	The Postman (Il Postino)	FALSE	1023
1997	actor in a leading role	Matt Damon	Good Will Hunting	FALSE	1024
2009	actor in a supporting role	Matt Damon	Invictus	FALSE	1025
2005	actor in a supporting role	Matt Dillon	Crash	FALSE	1026
1958	actress in a supporting role	Maureen Stapleton	Lonelyhearts	FALSE	1027
1970	actress in a supporting role	Maureen Stapleton	Airport	FALSE	1028
1978	actress in a supporting role	Maureen Stapleton	Interiors	FALSE	1029
1981	actress in a supporting role	Maureen Stapleton	Reds	TRUE	1030
1988	actor in a leading role	Max von Sydow	Pelle the Conqueror	FALSE	1031
2011	actor in a supporting role	Max von Sydow	Extremely Loud & Incredibly Close	FALSE	1032
1961	actor	Maximilian Schell	Judgment at Nuremberg	TRUE	1033
1975	actor	Maximilian Schell	The Man in the Glass Booth	FALSE	1034
1977	actor in a supporting role	Maximilian Schell	Julia	FALSE	1035
1985	actress in a supporting role	Meg Tilly	Agnes of God	FALSE	1036
1988	actress in a leading role	Melanie Griffith	Working Girl	FALSE	1037
1960	actress	Melina Mercouri	Never on Sunday	FALSE	1038
1977	actress in a supporting role	Melinda Dillon	Close Encounters of the Third Kind	FALSE	1039
1981	actress in a supporting role	Melinda Dillon	Absence of Malice	FALSE	1040
2008	actress in a leading role	Melissa Leo	Frozen River	FALSE	1041
2010	actress in a supporting role	Melissa Leo	The Fighter	TRUE	1042
2011	actress in a supporting role	Melissa McCarthy	Bridesmaids	FALSE	1043
1963	actor in a supporting role	Melvyn Douglas	Hud	TRUE	1044
1970	actor	Melvyn Douglas	I Never Sang for My Father	FALSE	1045
1979	actor in a supporting role	Melvyn Douglas	Being There	TRUE	1046
1949	actress in a supporting role	Mercedes McCambridge	All the King's Men	TRUE	1047
1956	actress in a supporting role	Mercedes McCambridge	Giant	FALSE	1048
1991	actress in a supporting role	Mercedes Ruehl	The Fisher King	TRUE	1049
1978	actress in a supporting role	Meryl Streep	The Deer Hunter	FALSE	1050
1979	actress in a supporting role	Meryl Streep	Kramer vs. Kramer	TRUE	1051
1981	actress in a leading role	Meryl Streep	The French Lieutenant's Woman	FALSE	1052
1982	actress in a leading role	Meryl Streep	Sophie's Choice	TRUE	1053
1983	actress in a leading role	Meryl Streep	Silkwood	FALSE	1054
1985	actress in a leading role	Meryl Streep	Out of Africa	FALSE	1055
1987	actress in a leading role	Meryl Streep	Ironweed	FALSE	1056
1988	actress in a leading role	Meryl Streep	A Cry in the Dark	FALSE	1057
1990	actress in a leading role	Meryl Streep	Postcards from the Edge	FALSE	1058
1995	actress in a leading role	Meryl Streep	The Bridges of Madison County	FALSE	1059
1998	actress in a leading role	Meryl Streep	One True Thing	FALSE	1060
1999	actress in a leading role	Meryl Streep	Music of the Heart	FALSE	1061
2002	actress in a supporting role	Meryl Streep	Adaptation	FALSE	1062
2006	actress in a leading role	Meryl Streep	The Devil Wears Prada	FALSE	1063
2008	actress in a leading role	Meryl Streep	Doubt	FALSE	1064
2009	actress in a leading role	Meryl Streep	Julie & Julia	FALSE	1065
2011	actress in a leading role	Meryl Streep	The Iron Lady	TRUE	1066
1966	actor	Michael Caine	Alfie	FALSE	1067
1972	actor	Michael Caine	Sleuth	FALSE	1068
1983	actor in a leading role	Michael Caine	Educating Rita	FALSE	1069
1986	actor in a supporting role	Michael Caine	Hannah and Her Sisters	TRUE	1070
1999	actor in a supporting role	Michael Caine	The Cider House Rules	TRUE	1071
2002	actor in a leading role	Michael Caine	The Quiet American	FALSE	1072
1945	actor in a supporting role	Michael Chekhov	Spellbound	FALSE	1073
1999	actor in a supporting role	Michael Clarke Duncan	The Green Mile	FALSE	1074
1987	actor in a leading role	Michael Douglas	Wall Street	TRUE	1075
1965	actor in a supporting role	Michael Dunn	Ship of Fools	FALSE	1076
1967	actor in a supporting role	Michael J. Pollard	Bonnie and Clyde	FALSE	1077
1991	actor in a supporting role	Michael Lerner	Barton Fink	FALSE	1078
1980	actor in a supporting role	Michael O'Keefe	The Great Santini	FALSE	1079
1947	actor	Michael Redgrave	Mourning Becomes Electra	FALSE	1080
2008	actor in a supporting role	Michael Shannon	Revolutionary Road	FALSE	1081
1974	actor in a supporting role	Michael V. Gazzo	The Godfather Part II	FALSE	1082
1988	actress in a supporting role	Michelle Pfeiffer	Dangerous Liaisons	FALSE	1083
1989	actress in a leading role	Michelle Pfeiffer	The Fabulous Baker Boys	FALSE	1084
1992	actress in a leading role	Michelle Pfeiffer	Love Field	FALSE	1085
2005	actress in a supporting role	Michelle Williams	Brokeback Mountain	FALSE	1086
2010	actress in a leading role	Michelle Williams	Blue Valentine	FALSE	1087
2011	actress in a leading role	Michelle Williams	My Week with Marilyn	FALSE	1088
1939	actor	Mickey Rooney	Babes in Arms	FALSE	1089
1943	actor	Mickey Rooney	The Human Comedy	FALSE	1090
1956	actor in a supporting role	Mickey Rooney	The Bold and the Brave	FALSE	1091
1979	actor in a supporting role	Mickey Rooney	The Black Stallion	FALSE	1092
2008	actor in a leading role	Mickey Rourke	The Wrestler	FALSE	1093
1977	actor in a supporting role	Mikhail Baryshnikov	The Turning Point	FALSE	1094
1951	actress in a supporting role	Mildred Dunnock	Death of a Salesman	FALSE	1095
1956	actress in a supporting role	Mildred Dunnock	Baby Doll	FALSE	1096
1967	actress in a supporting role	Mildred Natwick	Barefoot in the Park	FALSE	1097
1938	actress in a supporting role	Miliza Korjus	The Great Waltz	FALSE	1098
1997	actress in a supporting role	Minnie Driver	Good Will Hunting	FALSE	1099
1995	actress in a supporting role	Mira Sorvino	Mighty Aphrodite	TRUE	1100
1992	actress in a supporting role	Miranda Richardson	Damage	FALSE	1101
1994	actress in a leading role	Miranda Richardson	Tom & Viv	FALSE	1102
1936	actor in a supporting role	Mischa Auer	My Man Godfrey	FALSE	1103
1957	actress in a supporting role	Miyoshi Umeki	Sayonara	TRUE	1104
2009	actress in a supporting role	Mo'Nique	Precious: Based on the Novel 'Push' by Sapphire	TRUE	1105
1948	actor	Montgomery Clift	The Search	FALSE	1106
1951	actor	Montgomery Clift	A Place in the Sun	FALSE	1107
1953	actor	Montgomery Clift	From Here to Eternity	FALSE	1108
1961	actor in a supporting role	Montgomery Clift	Judgment at Nuremberg	FALSE	1109
1942	actor	Monty Woolley	The Pied Piper	FALSE	1110
1944	actor in a supporting role	Monty Woolley	Since You Went Away	FALSE	1111
1987	actor in a supporting role	Morgan Freeman	Street Smart	FALSE	1112
1989	actor in a leading role	Morgan Freeman	Driving Miss Daisy	FALSE	1113
1994	actor in a leading role	Morgan Freeman	The Shawshank Redemption	FALSE	1114
2004	actor in a supporting role	Morgan Freeman	Million Dollar Baby	TRUE	1115
2009	actor in a leading role	Morgan Freeman	Invictus	FALSE	1116
1956	actress	Nancy Kelly	The Bad Seed	FALSE	1117
1950	actress in a supporting role	Nancy Olson	Sunset Blvd.	FALSE	1118
2003	actress in a leading role	Naomi Watts	21 Grams	FALSE	1119
2012	actress in a leading role	Naomi Watts	The Impossible	FALSE	1120
2004	actress in a supporting role	Natalie Portman	Closer	FALSE	1121
2010	actress in a leading role	Natalie Portman	Black Swan	TRUE	1122
1955	actress in a supporting role	Natalie Wood	Rebel without a Cause	FALSE	1123
1961	actress	Natalie Wood	Splendor in the Grass	FALSE	1124
1963	actress	Natalie Wood	Love with the Proper Stranger	FALSE	1125
1976	actor in a supporting role	Ned Beatty	Network	FALSE	1126
1963	actor in a supporting role	Nick Adams	Twilight of Honor	FALSE	1127
1991	actor in a leading role	Nick Nolte	The Prince of Tides	FALSE	1128
1998	actor in a leading role	Nick Nolte	Affliction	FALSE	1129
2011	actor in a supporting role	Nick Nolte	Warrior	FALSE	1130
1995	actor in a leading role	Nicolas Cage	Leaving Las Vegas	TRUE	1131
2002	actor in a leading role	Nicolas Cage	Adaptation	FALSE	1132
2001	actress in a leading role	Nicole Kidman	Moulin Rouge	FALSE	1133
2002	actress in a leading role	Nicole Kidman	The Hours	TRUE	1134
2010	actress in a leading role	Nicole Kidman	Rabbit Hole	FALSE	1135
1994	actor in a leading role	Nigel Hawthorne	The Madness of King George	FALSE	1136
1954	actress in a supporting role	Nina Foch	Executive Suite	FALSE	1137
1984	actor in a supporting role	Noriyuki 'Pat' Morita	The Karate Kid	FALSE	1138
1987	actress in a supporting role	Norma Aleandro	Gaby - A True Story	FALSE	1139
1936	actress	Norma Shearer	Romeo and Juliet	FALSE	1140
1938	actress	Norma Shearer	Marie Antoinette	FALSE	1141
2011	actress in a supporting role	Octavia Spencer	The Help	TRUE	1142
1939	actress in a supporting role	Olivia de Havilland	Gone with the Wind	FALSE	1143
1941	actress	Olivia de Havilland	Hold Back the Dawn	FALSE	1144
1946	actress	Olivia de Havilland	To Each His Own	TRUE	1145
1948	actress	Olivia de Havilland	The Snake Pit	FALSE	1146
1949	actress	Olivia de Havilland	The Heiress	TRUE	1147
1987	actress in a supporting role	Olympia Dukakis	Moonstruck	TRUE	1148
1962	actor in a supporting role	Omar Sharif	Lawrence of Arabia	FALSE	1149
1985	actress in a supporting role	Oprah Winfrey	The Color Purple	FALSE	1150
1941	actor	Orson Welles	Citizen Kane	FALSE	1151
1948	actor in a supporting role	Oscar Homolka	I Remember Mama	FALSE	1152
1965	actor	Oskar Werner	Ship of Fools	FALSE	1153
2003	actress in a supporting role	Patricia Clarkson	Pieces of April	FALSE	1154
1941	actress in a supporting role	Patricia Collinge	The Little Foxes	FALSE	1155
1963	actress	Patricia Neal	Hud	TRUE	1156
1968	actress	Patricia Neal	The Subject Was Roses	FALSE	1157
1962	actress in a supporting role	Patty Duke	The Miracle Worker	TRUE	1158
1956	actress in a supporting role	Patty McCormack	The Bad Seed	FALSE	1159
2005	actor in a supporting role	Paul Giamatti	Cinderella Man	FALSE	1160
1943	actor	Paul Lukas	Watch on the Rhine	TRUE	1161
1936	actor	Paul Muni	The Story of Louis Pasteur	TRUE	1162
1937	actor	Paul Muni	The Life of Emile Zola	FALSE	1163
1959	actor	Paul Muni	The Last Angry Man	FALSE	1164
1958	actor	Paul Newman	Cat on a Hot Tin Roof	FALSE	1165
1961	actor	Paul Newman	The Hustler	FALSE	1166
1963	actor	Paul Newman	Hud	FALSE	1167
1967	actor	Paul Newman	Cool Hand Luke	FALSE	1168
1981	actor in a leading role	Paul Newman	Absence of Malice	FALSE	1169
1982	actor in a leading role	Paul Newman	The Verdict	FALSE	1170
1986	actor in a leading role	Paul Newman	The Color of Money	TRUE	1171
1994	actor in a leading role	Paul Newman	Nobody's Fool	FALSE	1172
2002	actor in a supporting role	Paul Newman	Road to Perdition	FALSE	1173
1966	actor	Paul Scofield	A Man for All Seasons	TRUE	1174
1994	actor in a supporting role	Paul Scofield	Quiz Show	FALSE	1175
1972	actor	Paul Winfield	Sounder	FALSE	1176
1943	actress in a supporting role	Paulette Goddard	So Proudly We Hail!	FALSE	1177
1989	actress in a leading role	Pauline Collins	Shirley Valentine	FALSE	1178
1984	actress in a supporting role	Peggy Ashcroft	A Passage to India	TRUE	1179
1958	actress in a supporting role	Peggy Cass	Auntie Mame	FALSE	1180
1955	actress in a supporting role	Peggy Lee	Pete Kelly's Blues	FALSE	1181
1965	actress in a supporting role	Peggy Wood	The Sound of Music	FALSE	1182
2006	actress in a leading role	Pen_lope Cruz	Volver	FALSE	1183
2008	actress in a supporting role	Pen_lope Cruz	Vicky Cristina Barcelona	TRUE	1184
2009	actress in a supporting role	Pen_lope Cruz	Nine	FALSE	1185
1978	actress in a supporting role	Penelope Milford	Coming Home	FALSE	1186
1993	actor in a supporting role	Pete Postlethwaite	In the Name of the Father	FALSE	1187
1960	actor in a supporting role	Peter Falk	Murder, Inc.	FALSE	1188
1961	actor in a supporting role	Peter Falk	Pocketful of Miracles	FALSE	1189
1971	actor	Peter Finch	Sunday Bloody Sunday	FALSE	1190
1976	actor in a leading role	Peter Finch	Network	TRUE	1191
1977	actor in a supporting role	Peter Firth	Equus	FALSE	1192
1997	actor in a leading role	Peter Fonda	Ulee's Gold	FALSE	1193
1962	actor	Peter O'Toole	Lawrence of Arabia	FALSE	1194
1964	actor	Peter O'Toole	Becket	FALSE	1195
1968	actor	Peter O'Toole	The Lion in Winter	FALSE	1196
1969	actor	Peter O'Toole	Goodbye, Mr. Chips	FALSE	1197
1972	actor	Peter O'Toole	The Ruling Class	FALSE	1198
1980	actor in a leading role	Peter O'Toole	The Stunt Man	FALSE	1199
1982	actor in a leading role	Peter O'Toole	My Favorite Year	FALSE	1200
2006	actor in a leading role	Peter O'Toole	Venus	FALSE	1201
1964	actor	Peter Sellers	Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb	FALSE	1202
1979	actor in a leading role	Peter Sellers	Being There	FALSE	1203
1951	actor in a supporting role	Peter Ustinov	Quo Vadis	FALSE	1204
1960	actor in a supporting role	Peter Ustinov	Spartacus	TRUE	1205
1964	actor in a supporting role	Peter Ustinov	Topkapi	TRUE	1206
2005	actor in a leading role	Philip Seymour Hoffman	Capote	TRUE	1207
2007	actor in a supporting role	Philip Seymour Hoffman	Charlie Wilson's War	FALSE	1208
2008	actor in a supporting role	Philip Seymour Hoffman	Doubt	FALSE	1209
2012	actor in a supporting role	Philip Seymour Hoffman	The Master	FALSE	1210
1961	actress	Piper Laurie	The Hustler	FALSE	1211
1976	actress in a supporting role	Piper Laurie	Carrie	FALSE	1212
1986	actress in a supporting role	Piper Laurie	Children of a Lesser God	FALSE	1213
2002	actress in a supporting role	Queen Latifah	Chicago	FALSE	1214
1977	actress in a supporting role	Quinn Cummings	The Goodbye Girl	FALSE	1215
2012	actress in a leading role	Quvenzhan_ Wallis	Beasts of the Southern Wild	FALSE	1216
1998	actress in a supporting role	Rachel Griffiths	Hilary and Jackie	FALSE	1217
1963	actress	Rachel Roberts	This Sporting Life	FALSE	1218
2005	actress in a supporting role	Rachel Weisz	The Constant Gardener	TRUE	1219
1937	actor in a supporting role	Ralph Bellamy	The Awful Truth	FALSE	1220
1993	actor in a supporting role	Ralph Fiennes	Schindler's List	FALSE	1221
1996	actor in a leading role	Ralph Fiennes	The English Patient	FALSE	1222
1949	actor in a supporting role	Ralph Richardson	The Heiress	FALSE	1223
1984	actor in a supporting role	Ralph Richardson	Greystoke: The Legend of Tarzan, Lord of the Apes	FALSE	1224
1973	actor in a supporting role	Randy Quaid	The Last Detail	FALSE	1225
1945	actor	Ray Milland	The Lost Weekend	TRUE	1226
1940	actor	Raymond Massey	Abe Lincoln in Illinois	FALSE	1227
1957	actor in a supporting role	Red Buttons	Sayonara	TRUE	1228
2005	actress in a leading role	Reese Witherspoon	Walk the Line	TRUE	1229
2001	actress in a leading role	Ren_e Zellweger	Bridget Jones's Diary	FALSE	1230
2002	actress in a leading role	Ren_e Zellweger	Chicago	FALSE	1231
2003	actress in a supporting role	Ren_e Zellweger	Cold Mountain	TRUE	1232
1963	actor	Rex Harrison	Cleopatra	FALSE	1233
1964	actor	Rex Harrison	My Fair Lady	TRUE	1234
1952	actor in a supporting role	Richard Burton	My Cousin Rachel	FALSE	1235
1953	actor	Richard Burton	The Robe	FALSE	1236
1964	actor	Richard Burton	Becket	FALSE	1237
1965	actor	Richard Burton	The Spy Who Came In from the Cold	FALSE	1238
1966	actor	Richard Burton	Who's Afraid of Virginia Woolf?	FALSE	1239
1969	actor	Richard Burton	Anne of the Thousand Days	FALSE	1240
1977	actor in a leading role	Richard Burton	Equus	FALSE	1241
1970	actor in a supporting role	Richard Castellano	Lovers and Other Strangers	FALSE	1242
1977	actor in a leading role	Richard Dreyfuss	The Goodbye Girl	TRUE	1243
1995	actor in a leading role	Richard Dreyfuss	Mr. Holland's Opus	FALSE	1244
1978	actor in a supporting role	Richard Farnsworth	Comes a Horseman	FALSE	1245
1999	actor in a leading role	Richard Farnsworth	The Straight Story	FALSE	1246
1963	actor	Richard Harris	This Sporting Life	FALSE	1247
1990	actor in a leading role	Richard Harris	The Field	FALSE	1248
1971	actor in a supporting role	Richard Jaeckel	Sometimes a Great Notion	FALSE	1249
2008	actor in a leading role	Richard Jenkins	The Visitor	FALSE	1250
1949	actor	Richard Todd	The Hasty Heart	FALSE	1251
1947	actor in a supporting role	Richard Widmark	Kiss of Death	FALSE	1252
2006	actress in a supporting role	Rinko Kikuchi	Babel	FALSE	1253
1983	actor in a supporting role	Rip Torn	Cross Creek	FALSE	1254
1961	actress in a supporting role	Rita Moreno	West Side Story	TRUE	1255
1988	actor in a supporting role	River Phoenix	Running on Empty	FALSE	1256
1974	actor in a supporting role	Robert De Niro	The Godfather Part II	TRUE	1257
1976	actor in a leading role	Robert De Niro	Taxi Driver	FALSE	1258
1978	actor in a leading role	Robert De Niro	The Deer Hunter	FALSE	1259
1980	actor in a leading role	Robert De Niro	Raging Bull	TRUE	1260
1990	actor in a leading role	Robert De Niro	Awakenings	FALSE	1261
1991	actor in a leading role	Robert De Niro	Cape Fear	FALSE	1262
2012	actor in a supporting role	Robert De Niro	Silver Linings Playbook	FALSE	1263
1938	actor	Robert Donat	The Citadel	FALSE	1264
1939	actor	Robert Donat	Goodbye, Mr. Chips	TRUE	1265
1992	actor in a leading role	Robert Downey Jr.	Chaplin	FALSE	1266
2008	actor in a supporting role	Robert Downey Jr.	Tropic Thunder	FALSE	1267
1972	actor in a supporting role	Robert Duvall	The Godfather	FALSE	1268
1979	actor in a supporting role	Robert Duvall	Apocalypse Now	FALSE	1269
1980	actor in a leading role	Robert Duvall	The Great Santini	FALSE	1270
1983	actor in a leading role	Robert Duvall	Tender Mercies	TRUE	1271
1997	actor in a leading role	Robert Duvall	The Apostle	FALSE	1272
1998	actor in a supporting role	Robert Duvall	A Civil Action	FALSE	1273
1997	actor in a supporting role	Robert Forster	Jackie Brown	FALSE	1274
1985	actor in a supporting role	Robert Loggia	Jagged Edge	FALSE	1275
1945	actor in a supporting role	Robert Mitchum	G. I. Joe	FALSE	1276
1937	actor	Robert Montgomery	Night Must Fall	FALSE	1277
1941	actor	Robert Montgomery	Here Comes Mr. Jordan	FALSE	1278
1938	actor in a supporting role	Robert Morley	Marie Antoinette	FALSE	1279
1982	actor in a supporting role	Robert Preston	Victor/Victoria	FALSE	1280
1973	actor	Robert Redford	The Sting	FALSE	1281
1947	actor in a supporting role	Robert Ryan	Crossfire	FALSE	1282
1966	actor in a supporting role	Robert Shaw	A Man for All Seasons	FALSE	1283
1956	actor in a supporting role	Robert Stack	Written on the Wind	FALSE	1284
1953	actor in a supporting role	Robert Strauss	Stalag 17	FALSE	1285
1959	actor in a supporting role	Robert Vaughn	The Young Philadelphians	FALSE	1286
1998	actor in a leading role	Roberto Benigni	Life Is Beautiful	TRUE	1287
1987	actor in a leading role	Robin Williams	Good Morning, Vietnam	FALSE	1288
1989	actor in a leading role	Robin Williams	Dead Poets Society	FALSE	1289
1991	actor in a leading role	Robin Williams	The Fisher King	FALSE	1290
1997	actor in a supporting role	Robin Williams	Good Will Hunting	TRUE	1291
1956	actor	Rock Hudson	Giant	FALSE	1292
1954	actor in a supporting role	Rod Steiger	On the Waterfront	FALSE	1293
1965	actor	Rod Steiger	The Pawnbroker	FALSE	1294
1967	actor	Rod Steiger	In the Heat of the Night	TRUE	1295
1937	actor in a supporting role	Roland Young	Topper	FALSE	1296
1968	actor	Ron Moody	Oliver!	FALSE	1297
1942	actor	Ronald Colman	Random Harvest	FALSE	1298
1947	actor	Ronald Colman	A Double Life	TRUE	1299
1975	actress in a supporting role	Ronee Blakley	Nashville	FALSE	1300
2011	actress in a leading role	Rooney Mara	The Girl with the Dragon Tattoo	FALSE	1301
1942	actress	Rosalind Russell	My Sister Eileen	FALSE	1302
1946	actress	Rosalind Russell	Sister Kenny	FALSE	1303
1947	actress	Rosalind Russell	Mourning Becomes Electra	FALSE	1304
1958	actress	Rosalind Russell	Auntie Mame	FALSE	1305
1994	actress in a supporting role	Rosemary Harris	Tom & Viv	FALSE	1306
1993	actress in a supporting role	Rosie Perez	Fearless	FALSE	1307
1971	actor in a supporting role	Roy Scheider	The French Connection	FALSE	1308
1979	actor in a leading role	Roy Scheider	All That Jazz	FALSE	1309
2007	actress in a supporting role	Ruby Dee	American Gangster	FALSE	1310
1969	actor in a supporting role	Rupert Crosse	The Reivers	FALSE	1311
1957	actor in a supporting role	Russ Tamblyn	Peyton Place	FALSE	1312
1999	actor in a leading role	Russell Crowe	The Insider	FALSE	1313
2000	actor in a leading role	Russell Crowe	Gladiator	TRUE	1314
2001	actor in a leading role	Russell Crowe	A Beautiful Mind	FALSE	1315
1965	actress in a supporting role	Ruth Gordon	Inside Daisy Clover	FALSE	1316
1968	actress in a supporting role	Ruth Gordon	Rosemary's Baby	TRUE	1317
1940	actress in a supporting role	Ruth Hussey	The Philadelphia Story	FALSE	1318
2006	actor in a leading role	Ryan Gosling	Half Nelson	FALSE	1319
1970	actor	Ryan O'Neal	Love Story	FALSE	1320
1955	actor in a supporting role	Sal Mineo	Rebel without a Cause	FALSE	1321
1960	actor in a supporting role	Sal Mineo	Exodus	FALSE	1322
1979	actress in a leading role	Sally Field	Norma Rae	TRUE	1323
1984	actress in a leading role	Sally Field	Places in the Heart	TRUE	1324
2012	actress in a supporting role	Sally Field	Lincoln	FALSE	1325
1970	actress in a supporting role	Sally Kellerman	M*A*S*H	FALSE	1326
1987	actress in a leading role	Sally Kirkland	Anna	FALSE	1327
2002	actress in a leading role	Salma Hayek	Frida	FALSE	1328
1950	actor in a supporting role	Sam Jaffe	The Asphalt Jungle	FALSE	1329
1983	actor in a supporting role	Sam Shepard	The Right Stuff	FALSE	1330
1984	actor in a leading role	Sam Waterston	The Killing Fields	FALSE	1331
1965	actress	Samantha Eggar	The Collector	FALSE	1332
1999	actress in a supporting role	Samantha Morton	Sweet and Lowdown	FALSE	1333
2003	actress in a leading role	Samantha Morton	In America	FALSE	1334
1994	actor in a supporting role	Samuel L. Jackson	Pulp Fiction	FALSE	1335
2009	actress in a leading role	Sandra Bullock	The Blind Side	TRUE	1336
1966	actress in a supporting role	Sandy Dennis	Who's Afraid of Virginia Woolf?	TRUE	1337
2007	actress in a supporting role	Saoirse Ronan	Atonement	FALSE	1338
1941	actress in a supporting role	Sara Allgood	How Green Was My Valley	FALSE	1339
1970	actress	Sarah Miles	Ryan's Daughter	FALSE	1340
1987	actor in a supporting role	Sean Connery	The Untouchables	TRUE	1341
1995	actor in a leading role	Sean Penn	Dead Man Walking	FALSE	1342
1999	actor in a leading role	Sean Penn	Sweet and Lowdown	FALSE	1343
2001	actor in a leading role	Sean Penn	I Am Sam	FALSE	1344
2003	actor in a leading role	Sean Penn	Mystic River	TRUE	1345
2008	actor in a leading role	Sean Penn	Milk	TRUE	1346
1957	actor in a supporting role	Sessue Hayakawa	The Bridge on the River Kwai	FALSE	1347
1968	actor in a supporting role	Seymour Cassel	Faces	FALSE	1348
1995	actress in a leading role	Sharon Stone	Casino	FALSE	1349
1951	actress	Shelley Winters	A Place in the Sun	FALSE	1350
1959	actress in a supporting role	Shelley Winters	The Diary of Anne Frank	TRUE	1351
1965	actress in a supporting role	Shelley Winters	A Patch of Blue	TRUE	1352
1972	actress in a supporting role	Shelley Winters	The Poseidon Adventure	FALSE	1353
1952	actress	Shirley Booth	Come Back, Little Sheba	TRUE	1354
1960	actress in a supporting role	Shirley Jones	Elmer Gantry	TRUE	1355
1960	actress in a supporting role	Shirley Knight	The Dark at the Top of the Stairs	FALSE	1356
1962	actress in a supporting role	Shirley Knight	Sweet Bird of Youth	FALSE	1357
1958	actress	Shirley MacLaine	Some Came Running	FALSE	1358
1960	actress	Shirley MacLaine	The Apartment	FALSE	1359
1963	actress	Shirley MacLaine	Irma La Douce	FALSE	1360
1977	actress in a leading role	Shirley MacLaine	The Turning Point	FALSE	1361
1983	actress in a leading role	Shirley MacLaine	Terms of Endearment	TRUE	1362
2003	actress in a supporting role	Shohreh Aghdashloo	House of Sand and Fog	FALSE	1363
1958	actor	Sidney Poitier	The Defiant Ones	FALSE	1364
1963	actor	Sidney Poitier	Lilies of the Field	TRUE	1365
1986	actress in a leading role	Sigourney Weaver	Aliens	FALSE	1366
1988	actress in a leading role	Sigourney Weaver	Gorillas in the Mist	FALSE	1367
1988	actress in a supporting role	Sigourney Weaver	Working Girl	FALSE	1368
1959	actress	Simone Signoret	Room at the Top	TRUE	1369
1965	actress	Simone Signoret	Ship of Fools	FALSE	1370
1956	actor	Sir Laurence Olivier	Richard III	FALSE	1371
1976	actress in a leading role	Sissy Spacek	Carrie	FALSE	1372
1980	actress in a leading role	Sissy Spacek	Coal Miner's Daughter	TRUE	1373
1982	actress in a leading role	Sissy Spacek	Missing	FALSE	1374
1984	actress in a leading role	Sissy Spacek	The River	FALSE	1375
1986	actress in a leading role	Sissy Spacek	Crimes of the Heart	FALSE	1376
2001	actress in a leading role	Sissy Spacek	In the Bedroom	FALSE	1377
1968	actress in a supporting role	Sondra Locke	The Heart Is a Lonely Hunter	FALSE	1378
1961	actress	Sophia Loren	Two Women	TRUE	1379
1964	actress	Sophia Loren	Marriage Italian Style	FALSE	1380
2004	actress in a supporting role	Sophie Okonedo	Hotel Rwanda	FALSE	1381
1936	actor	Spencer Tracy	San Francisco	FALSE	1382
1937	actor	Spencer Tracy	Captains Courageous	TRUE	1383
1938	actor	Spencer Tracy	Boys Town	TRUE	1384
1950	actor	Spencer Tracy	Father of the Bride	FALSE	1385
1955	actor	Spencer Tracy	Bad Day at Black Rock	FALSE	1386
1958	actor	Spencer Tracy	The Old Man and the Sea	FALSE	1387
1960	actor	Spencer Tracy	Inherit the Wind	FALSE	1388
1961	actor	Spencer Tracy	Judgment at Nuremberg	FALSE	1389
1967	actor	Spencer Tracy	Guess Who's Coming to Dinner	FALSE	1390
1938	actress in a supporting role	Spring Byington	You Can't Take It with You	FALSE	1391
1964	actor in a supporting role	Stanley Holloway	My Fair Lady	FALSE	1392
2009	actor in a supporting role	Stanley Tucci	The Lovely Bones	FALSE	1393
1992	actor in a leading role	Stephen Rea	The Crying Game	FALSE	1394
1966	actor	Steve McQueen	The Sand Pebbles	FALSE	1395
1993	actress in a leading role	Stockard Channing	Six Degrees of Separation	FALSE	1396
1936	actor in a supporting role	Stuart Erwin	Pigskin Parade	FALSE	1397
1961	actor	Stuart Whitman	The Mark	FALSE	1398
1947	actress	Susan Hayward	Smash-Up--The Story of a Woman	FALSE	1399
1949	actress	Susan Hayward	My Foolish Heart	FALSE	1400
1952	actress	Susan Hayward	With a Song in My Heart	FALSE	1401
1955	actress	Susan Hayward	I'll Cry Tomorrow	FALSE	1402
1958	actress	Susan Hayward	I Want to Live!	TRUE	1403
1959	actress in a supporting role	Susan Kohner	Imitation of Life	FALSE	1404
1942	actress in a supporting role	Susan Peters	Random Harvest	FALSE	1405
1981	actress in a leading role	Susan Sarandon	Atlantic City	FALSE	1406
1991	actress in a leading role	Susan Sarandon	Thelma & Louise	FALSE	1407
1992	actress in a leading role	Susan Sarandon	Lorenzo's Oil	FALSE	1408
1994	actress in a leading role	Susan Sarandon	The Client	FALSE	1409
1995	actress in a leading role	Susan Sarandon	Dead Man Walking	TRUE	1410
1972	actress in a supporting role	Susan Tyrrell	Fat City	FALSE	1411
1969	actress in a supporting role	Susannah York	They Shoot Horses, Don't They?	FALSE	1412
1941	actor in a supporting role	Sydney Greenstreet	The Maltese Falcon	FALSE	1413
1976	actor in a leading role	Sylvester Stallone	Rocky	FALSE	1414
1969	actress in a supporting role	Sylvia Miles	Midnight Cowboy	FALSE	1415
1975	actress in a supporting role	Sylvia Miles	Farewell, My Lovely	FALSE	1416
1973	actress in a supporting role	Sylvia Sidney	Summer Wishes, Winter Dreams	FALSE	1417
1974	actress in a supporting role	Talia Shire	The Godfather Part II	FALSE	1418
1976	actress in a leading role	Talia Shire	Rocky	FALSE	1419
2008	actress in a supporting role	Taraji P. Henson	The Curious Case of Benjamin Button	FALSE	1420
1973	actress in a supporting role	Tatum O'Neal	Paper Moon	TRUE	1421
1962	actor in a supporting role	Telly Savalas	Birdman of Alcatraz	FALSE	1422
1962	actor in a supporting role	Terence Stamp	Billy Budd	FALSE	1423
1941	actress in a supporting role	Teresa Wright	The Little Foxes	FALSE	1424
1942	actress	Teresa Wright	The Pride of the Yankees	FALSE	1425
1942	actress in a supporting role	Teresa Wright	Mrs. Miniver	TRUE	1426
1982	actress in a supporting role	Teri Garr	Tootsie	FALSE	1427
2005	actor in a leading role	Terrence Howard	Hustle & Flow	FALSE	1428
1952	actress in a supporting role	Terry Moore	Come Back, Little Sheba	FALSE	1429
1986	actress in a supporting role	Tess Harper	Crimes of the Heart	FALSE	1430
1950	actress in a supporting role	Thelma Ritter	All about Eve	FALSE	1431
1951	actress in a supporting role	Thelma Ritter	The Mating Season	FALSE	1432
1952	actress in a supporting role	Thelma Ritter	With a Song in My Heart	FALSE	1433
1953	actress in a supporting role	Thelma Ritter	Pickup on South Street	FALSE	1434
1959	actress in a supporting role	Thelma Ritter	Pillow Talk	FALSE	1435
1962	actress in a supporting role	Thelma Ritter	Birdman of Alcatraz	FALSE	1436
1958	actor in a supporting role	Theodore Bikel	The Defiant Ones	FALSE	1437
1947	actor in a supporting role	Thomas Gomez	Ride the Pink Horse	FALSE	1438
2004	actor in a supporting role	Thomas Haden Church	Sideways	FALSE	1439
1937	actor in a supporting role	Thomas Mitchell	The Hurricane	FALSE	1440
1939	actor in a supporting role	Thomas Mitchell	Stagecoach	TRUE	1441
2007	actress in a supporting role	Tilda Swinton	Michael Clayton	TRUE	1442
2003	actor in a supporting role	Tim Robbins	Mystic River	TRUE	1443
1995	actor in a supporting role	Tim Roth	Rob Roy	FALSE	1444
1980	actor in a supporting role	Timothy Hutton	Ordinary People	TRUE	1445
1986	actor in a supporting role	Tom Berenger	Platoon	FALSE	1446
1983	actor in a leading role	Tom Conti	Reuben, Reuben	FALSE	1447
1965	actor in a supporting role	Tom Courtenay	Doctor Zhivago	FALSE	1448
1983	actor in a leading role	Tom Courtenay	The Dresser	FALSE	1449
1989	actor in a leading role	Tom Cruise	Born on the Fourth of July	FALSE	1450
1996	actor in a leading role	Tom Cruise	Jerry Maguire	FALSE	1451
1999	actor in a supporting role	Tom Cruise	Magnolia	FALSE	1452
1988	actor in a leading role	Tom Hanks	Big	FALSE	1453
1993	actor in a leading role	Tom Hanks	Philadelphia	TRUE	1454
1994	actor in a leading role	Tom Hanks	Forrest Gump	TRUE	1455
1998	actor in a leading role	Tom Hanks	Saving Private Ryan	FALSE	1456
2000	actor in a leading role	Tom Hanks	Cast Away	FALSE	1457
1984	actor in a leading role	Tom Hulce	Amadeus	FALSE	1458
1954	actor in a supporting role	Tom Tully	The Caine Mutiny	FALSE	1459
2001	actor in a leading role	Tom Wilkinson	In the Bedroom	FALSE	1460
2007	actor in a supporting role	Tom Wilkinson	Michael Clayton	FALSE	1461
1991	actor in a supporting role	Tommy Lee Jones	JFK	FALSE	1462
1993	actor in a supporting role	Tommy Lee Jones	The Fugitive	TRUE	1463
2007	actor in a leading role	Tommy Lee Jones	In the Valley of Elah	FALSE	1464
2012	actor in a supporting role	Tommy Lee Jones	Lincoln	FALSE	1465
1999	actress in a supporting role	Toni Collette	The Sixth Sense	FALSE	1466
1958	actor	Tony Curtis	The Defiant Ones	FALSE	1467
1971	actor	Topol	Fiddler on the Roof	FALSE	1468
1960	actor	Trevor Howard	Sons and Lovers	FALSE	1469
1977	actress in a supporting role	Tuesday Weld	Looking for Mr. Goodbar	FALSE	1470
1994	actress in a supporting role	Uma Thurman	Pulp Fiction	FALSE	1471
1961	actress in a supporting role	Una Merkel	Summer and Smoke	FALSE	1472
1974	actress in a supporting role	Valentina Cortese	Day for Night	FALSE	1473
1974	actress	Valerie Perrine	Lenny	FALSE	1474
1942	actor in a supporting role	Van Heflin	Johnny Eager	TRUE	1475
1966	actress	Vanessa Redgrave	Morgan!	FALSE	1476
1968	actress	Vanessa Redgrave	Isadora	FALSE	1477
1971	actress	Vanessa Redgrave	Mary, Queen of Scots	FALSE	1478
1977	actress in a supporting role	Vanessa Redgrave	Julia	TRUE	1479
1984	actress in a leading role	Vanessa Redgrave	The Bostonians	FALSE	1480
1992	actress in a supporting role	Vanessa Redgrave	Howards End	FALSE	1481
2009	actress in a supporting role	Vera Farmiga	Up in the Air	FALSE	1482
1962	actor in a supporting role	Victor Buono	What Ever Happened to Baby Jane?	FALSE	1483
1952	actor in a supporting role	Victor McLaglen	The Quiet Man	FALSE	1484
2007	actor in a leading role	Viggo Mortensen	Eastern Promises	FALSE	1485
1973	actor in a supporting role	Vincent Gardenia	Bang the Drum Slowly	FALSE	1486
1987	actor in a supporting role	Vincent Gardenia	Moonstruck	FALSE	1487
2008	actress in a supporting role	Viola Davis	Doubt	FALSE	1488
2011	actress in a leading role	Viola Davis	The Help	FALSE	1489
2004	actress in a supporting role	Virginia Madsen	Sideways	FALSE	1490
1957	actor in a supporting role	Vittorio De Sica	A Farewell to Arms	FALSE	1491
1939	actress	Vivien Leigh	Gone with the Wind	TRUE	1492
1951	actress	Vivien Leigh	A Streetcar Named Desire	TRUE	1493
1966	actress in a supporting role	Vivien Merchant	Alfie	FALSE	1494
1936	actor in a supporting role	Walter Brennan	Come and Get It	TRUE	1495
1938	actor in a supporting role	Walter Brennan	Kentucky	TRUE	1496
1940	actor in a supporting role	Walter Brennan	The Westerner	TRUE	1497
1941	actor in a supporting role	Walter Brennan	Sergeant York	FALSE	1498
1936	actor	Walter Huston	Dodsworth	FALSE	1499
1941	actor	Walter Huston	All That Money Can Buy	FALSE	1500
1942	actor in a supporting role	Walter Huston	Yankee Doodle Dandy	FALSE	1501
1948	actor in a supporting role	Walter Huston	The Treasure of the Sierra Madre	TRUE	1502
1966	actor in a supporting role	Walter Matthau	The Fortune Cookie	TRUE	1503
1971	actor	Walter Matthau	Kotch	FALSE	1504
1975	actor	Walter Matthau	The Sunshine Boys	FALSE	1505
1942	actor	Walter Pidgeon	Mrs. Miniver	FALSE	1506
1943	actor	Walter Pidgeon	Madame Curie	FALSE	1507
1967	actor	Warren Beatty	Bonnie and Clyde	FALSE	1508
1978	actor in a leading role	Warren Beatty	Heaven Can Wait	FALSE	1509
1981	actor in a leading role	Warren Beatty	Reds	FALSE	1510
1991	actor in a leading role	Warren Beatty	Bugsy	FALSE	1511
1938	actress	Wendy Hiller	Pygmalion	FALSE	1512
1958	actress in a supporting role	Wendy Hiller	Separate Tables	TRUE	1513
1966	actress in a supporting role	Wendy Hiller	A Man for All Seasons	FALSE	1514
1985	actress in a leading role	Whoopi Goldberg	The Color Purple	FALSE	1515
1990	actress in a supporting role	Whoopi Goldberg	Ghost	TRUE	1516
2001	actor in a leading role	Will Smith	Ali	FALSE	1517
2006	actor in a leading role	Will Smith	The Pursuit of Happyness	FALSE	1518
1986	actor in a supporting role	Willem Dafoe	Platoon	FALSE	1519
2000	actor in a supporting role	Willem Dafoe	Shadow of the Vampire	FALSE	1520
1942	actor in a supporting role	William Bendix	Wake Island	FALSE	1521
1946	actor in a supporting role	William Demarest	The Jolson Story	FALSE	1522
1940	actor in a supporting role	William Gargan	They Knew What They Wanted	FALSE	1523
1996	actor in a supporting role	William H. Macy	Fargo	FALSE	1524
1985	actor in a supporting role	William Hickey	Prizzi's Honor	FALSE	1525
1950	actor	William Holden	Sunset Blvd.	FALSE	1526
1953	actor	William Holden	Stalag 17	TRUE	1527
1976	actor in a leading role	William Holden	Network	FALSE	1528
1985	actor in a leading role	William Hurt	Kiss of the Spider Woman	TRUE	1529
1986	actor in a leading role	William Hurt	Children of a Lesser God	FALSE	1530
1987	actor in a leading role	William Hurt	Broadcast News	FALSE	1531
2005	actor in a supporting role	William Hurt	A History of Violence	FALSE	1532
1936	actor	William Powell	My Man Godfrey	FALSE	1533
1947	actor	William Powell	Life with Father	FALSE	1534
1993	actress in a supporting role	Winona Ryder	The Age of Innocence	FALSE	1535
1994	actress in a leading role	Winona Ryder	Little Women	FALSE	1536
1977	actor in a leading role	Woody Allen	Annie Hall	FALSE	1537
1996	actor in a leading role	Woody Harrelson	The People vs. Larry Flynt	FALSE	1538
2009	actor in a supporting role	Woody Harrelson	The Messenger	FALSE	1539
1956	actor	Yul Brynner	The King and I	TRUE	1540
year:
bigint
category:
string
nominee:
string
movie:
string
winner:
boolean
id:
bigint
nominee_information
Preview
name	amg_person_id	top_genre	birthday	id
Ruby Dee	P 18243	Drama	1924-10-27	234
Hal Holbrook	P 32790	Drama	1925-02-17	241
Cloris Leachman	P 41211	Comedy	1926-04-30	257
Rosemary Harris	P 30676	Drama	1930-09-19	301
Martin Landau	P 40247	Spy Film	1931-06-20	312
Ian Holm	P 32962	Drama	1931-09-12	315
Debbie Reynolds	P 59782	Comedy	1932-04-01	321
Michael Caine	P 10198	Thriller	1933-03-14	335
Alan Alda	P 79264	Comedy	1936-01-28	366
Albert Finney	P 23545	Drama	1936-05-09	371
Morgan Freeman	P 90514	Drama	1937-06-01	386
Anthony Hopkins	P 94812	Drama	1937-12-31	391
Ian McKellen	P 47684	Drama	1939-05-25	409
Tom Conti	P 14627	Drama	1941-11-22	437
Bob Hoskins	P 33185	Drama	1942-10-26	447
Joe Pesci	P 56237	Comedy	1943-02-09	448
Robert De Niro	P 17593	Drama	1943-08-17	452
Sam Shepard	P111142	Drama	1943-11-05	456
Ben Kingsley	P 38383	Drama	1943-12-31	458
Gary Busey	P  9844	Drama	1944-06-29	463
Michael Douglas	P 88134	Drama	1944-09-25	464
Sally Kirkland	P 38510	Drama	1944-10-31	465
Helen Mirren	P 49576	Drama	1945-07-26	471
Diane Keaton	P 96996	Comedy	1946-01-05	476
Bruce Davison	P 17454	Drama	1946-06-28	482
Tommy Lee Jones	P 36238	Drama	1946-09-15	485
Stephen Rea	P 59079	Drama	1946-10-31	488
Sally Field	P 89714	Comedy	1946-11-06	489
Richard Jenkins	P 35464	Drama	1947-05-04	494
Kevin Kline	P 38699	Comedy	1947-10-24	500
Dianne Wiest	P 76163	Drama	1948-03-28	506
Kathy Bates	P  4516	Drama	1948-06-28	508
Samuel L. Jackson	P 34866	Drama	1948-12-21	511
Gerard Depardieu	P 87517	Drama	1948-12-27	512
David Strathairn	P 68638	Drama	1949-01-26	513
Jessica Lange	P 40447	Drama	1949-04-20	514
Jim Broadbent	P  8575	Drama	1949-05-24	515
Sigourney Weaver	P 75144	Comedy	1949-10-08	518
Jeff Bridges	P  3197	Drama	1949-12-04	519
Julie Walters	P 74515	Drama	1950-02-22	521
Ed Harris	P 30614	Drama	1950-11-28	531
Chazz Palminteri	P 54860	Drama	1952-05-15	540
Liam Neeson	P 52070	Drama	1952-06-07	541
Dan Aykroyd	P 80282	Comedy	1952-07-01	544
Denzel Washington	P 74843	Drama	1954-12-28	562
Kevin Costner	P 15189	History [nf]	1955-01-18	563
Willem Dafoe	P 16547	Drama	1955-07-22	570
Whoopi Goldberg	P 27431	Comedy	1955-11-13	573
Joan Allen	P  1026	Drama	1956-08-20	580
Christoph Waltz	P221135	Drama	1956-10-04	581
Daniel Day Lewis	P 17559	Drama	1957-04-29	582
Daniel Day-Lewis	P 17559	Drama	1957-04-29	583
Frances McDormand	P 47305	Drama	1957-06-23	584
Sharon Stone	P 68496	Drama	1958-03-10	588
Gary Oldman	P 53946	Drama	1958-03-21	590
Alec Baldwin	P  3515	Comedy	1958-04-03	591
Michelle Pfeiffer	P 56469	Drama	1958-04-29	592
Angela Bassett	P  4466	Drama	1958-08-16	594
Viggo Mortensen	P 50903	Drama	1958-10-20	597
Catherine Keener	P 37341	Comedy	1959-03-26	600
Emma Thompson	P 70692	Drama	1959-04-15	601
John Hawkes	P 31099	Comedy	1959-09-11	605
Ken Watanabe	P 74900	Drama	1959-10-21	606
Stanley Tucci	P 72023	Comedy	1960-01-11	608
Thomas Haden Church	P195520	Comedy	1960-06-17	611
Colin Firth	P 23590	Drama	1960-09-10	614
Melissa Leo	P 41835	Drama	1960-09-14	615
Eddie Murphy	P 51440	Comedy	1961-04-03	620
George Clooney	P 13722	Comedy	1961-05-06	622
Jackie Earle Haley	P 29701	Comedy	1961-07-14	625
Woody Harrelson	P 30548	Comedy	1961-07-23	628
Laurence Fishburne	P 23625	Drama	1961-07-30	629
Tom Cruise	P 86295	Drama	1962-07-03	631
Jodie Foster	P 90220	Drama	1962-11-19	633
Ralph Fiennes	P 23390	Drama	1962-12-22	635
Johnny Depp	P 18682	Drama	1963-06-09	636
Brad Pitt	P 56988	Drama	1963-12-18	643
Nicolas Cage	P 10155	Drama	1964-01-07	644
Matt Dillon	P 19210	Drama	1964-02-18	646
Juliette Binoche	P  6261	Drama	1964-03-09	647
Russell Crowe	P 15959	Drama	1964-04-07	648
Djimon Hounsou	P 33391	Drama	1964-04-24	649
Sandra Bullock	P  9472	Comedy	1964-07-26	650
Rosie Perez	P106101	Drama	1964-09-06	651
Don Cheadle	P 12587	Drama	1964-11-29	653
Diane Lane	P 40350	Drama	1965-01-22	655
Robert Downey Jr.	P 19966	Comedy	1965-04-04	656
Helena Bonham Carter	P  7266	Drama	1966-05-26	660
Paul Giamatti	P 26680	Comedy	1967-06-06	667
Nicole Kidman	P 38065	Drama	1967-06-20	668
Mark Ruffalo	P197651	Drama	1967-11-22	673
Jamie Foxx	P 24604	Comedy	1967-12-13	675
Cuba Gooding Jr.	P 27665	Drama	1968-01-02	677
Josh Brolin	P  8657	Drama	1968-02-12	678
Will Smith	P 66596	Comedy	1968-09-25	681
Hugh Jackman	P269258	Action	1968-10-12	683
Javier Bardem	P  3887	Drama	1969-03-01	684
Terrence Howard	P 33528	Drama	1969-03-11	685
Cate Blanchett	P215038	Drama	1969-05-14	687
Edward Norton	P215904	Drama	1969-08-18	688
Catherine Zeta-Jones	P 36062	Comedy	1969-09-25	689
Queen Latifah	P 40714	Comedy	1970-03-18	692
Matt Damon	P 16762	Drama	1970-10-08	698
Jeremy Renner	P199226	Drama	1971-01-07	701
Rachel Weisz	P216376	Drama	1971-03-07	702
Winona Ryder	P 62446	Drama	1971-10-29	705
Gwyneth Paltrow	P 54871	Drama	1972-09-28	707
Toni Collette	P 14165	Drama	1972-11-01	708
Vera Farmiga	P241678	Drama	1973-08-06	712
Christian Bale	P  3538	Drama	1974-01-30	713
Michael Shannon	P516240	Drama	1974-08-07	716
Charlize Theron	P216257	Drama	1975-08-07	722
Amy Adams	P273224	Comedy	1975-08-20	724
Marion Cotillard	P195575	Drama	1975-09-30	726
Reese Witherspoon	P 77086	Comedy	1976-03-22	728
Jessica Chastain	P470479	Adventure	1977-03-29	730
Samantha Morton	P230665	Drama	1977-05-13	731
James Franco	P299361	Drama	1978-04-19	733
Kate Hudson	P263367	Comedy	1979-04-19	735
Michelle Williams	P198320	Drama	1980-09-09	736
Ryan Gosling	P279096	Drama	1980-11-12	737
Rinko Kikuchi	P475244	Drama	1981-01-06	739
Jennifer Hudson	P454405	Drama	1981-09-12	742
Anne Hathaway	P292630	Drama	1982-11-12	744
Jonah Hill	P418718	Comedy	1983-12-20	747
Jennifer Lawrence	P562566	Drama	1990-08-15	755
Ingrid Bergman	P999996	Drama	1915-08-29	1541
name:
string
amg_person_id:
string
top_genre:
string
birthday:
date
id:
bigint
'''


# Import your libraries
import pyspark
from pyspark.sql.functions import *
# Start writing code
df=oscar_nominees
df1=nominee_information

df2=df.join(df1,df.nominee==df1.name)
df2=df2.filter(df2.winner==True)
df2=df2.groupby("top_genre").agg(count("winner").alias("cnt"))
df2=df2.orderBy(desc("cnt")).limit(1).select("top_genre")
# df2.show(truncate=False)
df2.toPandas()

# To validate your solution, convert your final pySpark df to a pandas df
# oscar_nominees.toPandas()