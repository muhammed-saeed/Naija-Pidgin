import os
en_path = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\en_bible\en\\"
pcm_path = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\pcm_bible\pcm\\"
files = os.listdir(
    en_path)
verses_out = []
dump = []
books_to_be_solved = [['4_1.txt', '4_2.txt', '4_3.txt', '4_4.txt', '4_5.txt', '4_6.txt', '4_7.txt', '4_8.txt', '4_9.txt', '4_10.txt', '4_11.txt', '4_12.txt', '4_13.txt', '4_14.txt', '4_15.txt', '4_16.txt', '4_17.txt', '4_18.txt', '4_19.txt', '4_20.txt', '4_21.txt', '4_22.txt', '4_23.txt', '4_24.txt', '4_25.txt', '4_26.txt', '4_27.txt', '4_28.txt', '4_29.txt', '4_30.txt', '4_31.txt', '4_32.txt', '4_33.txt', '4_34.txt', '4_35.txt', '4_36.txt'], ['19_2.txt', '19_3.txt', '19_4.txt', '19_5.txt', '19_6.txt', '19_7.txt', '19_8.txt', '19_9.txt', '19_10.txt', '19_11.txt', '19_12.txt', '19_13.txt', '19_14.txt', '19_15.txt', '19_16.txt', '19_17.txt', '19_18.txt', '19_19.txt', '19_20.txt', '19_21.txt', '19_22.txt', '19_23.txt', '19_24.txt', '19_25.txt', '19_26.txt', '19_27.txt', '19_28.txt', '19_29.txt', '19_30.txt', '19_31.txt', '19_32.txt', '19_33.txt', '19_34.txt', '19_35.txt', '19_36.txt', '19_37.txt', '19_38.txt', '19_39.txt', '19_40.txt', '19_41.txt', '19_42.txt', '19_43.txt', '19_44.txt', '19_45.txt', '19_46.txt', '19_47.txt', '19_48.txt', '19_49.txt', '19_50.txt', '19_51.txt', '19_52.txt', '19_53.txt', '19_54.txt', '19_55.txt', '19_56.txt', '19_57.txt', '19_58.txt', '19_59.txt', '19_60.txt', '19_61.txt', '19_62.txt', '19_63.txt', '19_64.txt', '19_65.txt', '19_66.txt', '19_67.txt', '19_68.txt', '19_69.txt', '19_70.txt', '19_71.txt',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                '19_72.txt', '19_73.txt', '19_74.txt', '19_75.txt', '19_76.txt', '19_77.txt', '19_78.txt', '19_79.txt', '19_80.txt', '19_81.txt', '19_82.txt', '19_83.txt', '19_84.txt', '19_85.txt', '19_86.txt', '19_87.txt', '19_88.txt', '19_89.txt', '19_90.txt', '19_91.txt', '19_92.txt', '19_93.txt', '19_94.txt', '19_95.txt', '19_96.txt', '19_97.txt', '19_98.txt', '19_99.txt', '19_100.txt', '19_101.txt', '19_102.txt', '19_103.txt', '19_104.txt', '19_105.txt', '19_106.txt', '19_107.txt', '19_108.txt', '19_109.txt', '19_110.txt', '19_111.txt', '19_112.txt', '19_113.txt', '19_114.txt', '19_115.txt', '19_116.txt', '19_117.txt', '19_118.txt', '19_119.txt', '19_120.txt', '19_121.txt', '19_122.txt', '19_123.txt', '19_124.txt', '19_125.txt', '19_126.txt', '19_127.txt', '19_128.txt', '19_129.txt', '19_130.txt', '19_131.txt', '19_132.txt', '19_133.txt', '19_134.txt', '19_135.txt', '19_136.txt', '19_137.txt', '19_138.txt', '19_139.txt', '19_140.txt', '19_141.txt', '19_142.txt', '19_143.txt', '19_144.txt', '19_145.txt', '19_146.txt', '19_147.txt', '19_148.txt', '19_149.txt', '19_150.txt'], ['66_1.txt', '66_2.txt', '66_3.txt', '66_4.txt', '66_5.txt', '66_6.txt', '66_7.txt', '66_8.txt', '66_9.txt', '66_10.txt', '66_11.txt', '66_12.txt', '66_13.txt', '66_14.txt', '66_15.txt', '66_16.txt', '66_17.txt', '66_18.txt', '66_19.txt', '66_20.txt', '66_21.txt', '66_22.txt']]


two_chapters = []
two_chapters.append(books_to_be_solved[0])
two_chapters.append(books_to_be_solved[2])

pcm_chapter_19 = ['19_2.txt', '19_3.txt', '19_4.txt', '19_5.txt', '19_6.txt', '19_7.txt', '19_8.txt', '19_9.txt', '19_10.txt', '19_11.txt', '19_12.txt', '19_13.txt', '19_14.txt', '19_15.txt', '19_16.txt', '19_17.txt', '19_18.txt', '19_19.txt', '19_20.txt', '19_21.txt', '19_22.txt', '19_23.txt', '19_24.txt', '19_25.txt', '19_26.txt', '19_27.txt', '19_28.txt', '19_29.txt', '19_30.txt', '19_31.txt', '19_32.txt', '19_33.txt', '19_34.txt', '19_35.txt', '19_36.txt', '19_37.txt', '19_38.txt', '19_39.txt', '19_40.txt', '19_41.txt', '19_42.txt', '19_43.txt', '19_44.txt', '19_45.txt', '19_46.txt', '19_47.txt', '19_48.txt', '19_49.txt', '19_50.txt', '19_51.txt', '19_52.txt', '19_53.txt', '19_54.txt', '19_55.txt', '19_56.txt', '19_57.txt', '19_58.txt', '19_59.txt', '19_60.txt', '19_61.txt', '19_62.txt', '19_63.txt', '19_64.txt', '19_65.txt', '19_66.txt', '19_67.txt', '19_68.txt', '19_69.txt', '19_70.txt', '19_71.txt',
                  '19_72.txt', '19_73.txt', '19_74.txt', '19_75.txt', '19_76.txt', '19_77.txt', '19_78.txt', '19_79.txt', '19_80.txt', '19_81.txt', '19_82.txt', '19_83.txt', '19_84.txt', '19_85.txt', '19_86.txt', '19_87.txt', '19_88.txt', '19_89.txt', '19_90.txt', '19_91.txt', '19_92.txt', '19_93.txt', '19_94.txt', '19_95.txt', '19_96.txt', '19_97.txt', '19_98.txt', '19_99.txt', '19_100.txt', '19_101.txt', '19_102.txt', '19_103.txt', '19_104.txt', '19_105.txt', '19_106.txt', '19_107.txt', '19_108.txt', '19_109.txt', '19_110.txt', '19_111.txt', '19_112.txt', '19_113.txt', '19_114.txt', '19_115.txt', '19_116.txt', '19_117.txt', '19_118.txt', '19_119.txt', '19_120.txt', '19_121.txt', '19_122.txt', '19_123.txt', '19_124.txt', '19_125.txt', '19_126.txt', '19_127.txt', '19_128.txt', '19_129.txt', '19_130.txt', '19_131.txt', '19_132.txt', '19_133.txt', '19_134.txt', '19_135.txt', '19_136.txt', '19_137.txt', '19_138.txt', '19_139.txt', '19_140.txt', '19_141.txt', '19_142.txt', '19_143.txt', '19_144.txt', '19_145.txt', '19_146.txt', '19_147.txt', '19_148.txt', '19_149.txt', '19_150.txt', '19_151.txt']

en_chapters_19 = ['19_1.txt', '19_2.txt', '19_3.txt', '19_4.txt', '19_5.txt', '19_6.txt', '19_7.txt', '19_8.txt', '19_9.txt', '19_10.txt', '19_11.txt', '19_12.txt', '19_13.txt', '19_14.txt', '19_15.txt', '19_16.txt', '19_17.txt', '19_18.txt', '19_19.txt', '19_20.txt', '19_21.txt', '19_22.txt', '19_23.txt', '19_24.txt', '19_25.txt', '19_26.txt', '19_27.txt', '19_28.txt', '19_29.txt', '19_30.txt', '19_31.txt', '19_32.txt', '19_33.txt', '19_34.txt', '19_35.txt', '19_36.txt', '19_37.txt', '19_38.txt', '19_39.txt', '19_40.txt', '19_41.txt', '19_42.txt', '19_43.txt', '19_44.txt', '19_45.txt', '19_46.txt', '19_47.txt', '19_48.txt', '19_49.txt', '19_50.txt', '19_51.txt', '19_52.txt', '19_53.txt', '19_54.txt', '19_55.txt', '19_56.txt', '19_57.txt', '19_58.txt', '19_59.txt', '19_60.txt', '19_61.txt', '19_62.txt', '19_63.txt', '19_64.txt', '19_65.txt', '19_66.txt', '19_67.txt', '19_68.txt', '19_69.txt', '19_70.txt', '19_71.txt',
                  '19_72.txt', '19_73.txt', '19_74.txt', '19_75.txt', '19_76.txt', '19_77.txt', '19_78.txt', '19_79.txt', '19_80.txt', '19_81.txt', '19_82.txt', '19_83.txt', '19_84.txt', '19_85.txt', '19_86.txt', '19_87.txt', '19_88.txt', '19_89.txt', '19_90.txt', '19_91.txt', '19_92.txt', '19_93.txt', '19_94.txt', '19_95.txt', '19_96.txt', '19_97.txt', '19_98.txt', '19_99.txt', '19_100.txt', '19_101.txt', '19_102.txt', '19_103.txt', '19_104.txt', '19_105.txt', '19_106.txt', '19_107.txt', '19_108.txt', '19_109.txt', '19_110.txt', '19_111.txt', '19_112.txt', '19_113.txt', '19_114.txt', '19_115.txt', '19_116.txt', '19_117.txt', '19_118.txt', '19_119.txt', '19_120.txt', '19_121.txt', '19_122.txt', '19_123.txt', '19_124.txt', '19_125.txt', '19_126.txt', '19_127.txt', '19_128.txt', '19_129.txt', '19_130.txt', '19_131.txt', '19_132.txt', '19_133.txt', '19_134.txt', '19_135.txt', '19_136.txt', '19_137.txt', '19_138.txt', '19_139.txt', '19_140.txt', '19_141.txt', '19_142.txt', '19_143.txt', '19_144.txt', '19_145.txt', '19_146.txt', '19_147.txt', '19_148.txt', '19_149.txt', '19_150.txt']


for i in range(150):
    en_verse_path = en_path +   en_chapters_19[i]
    en_counter = 0
    en_verse = ""
    with open(en_verse_path, "r") as fb:
        en_verse = fb.readlines()
    pcm_verse_path = pcm_path + pcm_chapter_19[i]
    pcm_counter = 0
    pcm_verse = ""
    with open(pcm_verse_path, "r", encoding="utf-8") as fb:
        pcm_verse = fb.readlines()

    if len(pcm_verse) != len(en_verse):
        dump.append(i)
verses_out.append(dump)
print(verses_out)

# print(two_chapters)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&777")
for book in two_chapters:
    dump = []
    for verse in book:
        en_verse_path = en_path + verse
        en_counter = 0
        en_verse = ""
        with open(en_verse_path, "r") as fb:
            en_verse = fb.readlines()
        pcm_verse_path = pcm_path + verse
        pcm_counter = 0
        pcm_verse = ""
        with open(pcm_verse_path, "r", encoding="utf-8") as fb:
            pcm_verse = fb.readlines()

        if len(pcm_verse) != len(en_verse):
            dump.append(verse)
    verses_out.append(dump)
print(verses_out)

solving_chapter_19_arr = verses_out[0]
solving_chapter_19_arr.append(1)
print(solving_chapter_19_arr)

chapter_19_path_pcm = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\pcm_bible\chapter_19.txt"
chapter_19_path_en = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\en_bible\chapter_19.txt"
for i in range(150):
    if i not in solving_chapter_19_arr:
        en_verse_path = en_path + en_chapters_19[i]
        en_counter = 0
        en_verse = ""
        with open(en_verse_path, "r") as fb:
            en_verse = fb.readlines()
        with open(chapter_19_path_en, "a") as fb:
            fb.writelines(en_verse)
        pcm_verse_path = pcm_path + pcm_chapter_19[i]
        pcm_counter = 0
        pcm_verse = ""
        with open(pcm_verse_path, "r") as fb:
            pcm_verse = fb.readlines()
        with open(chapter_19_path_pcm, "a") as fb:
            fb.writelines(pcm_verse)


two_capters_problems = ['4_1.txt', '66_12.txt']
path_en = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\en_bible\c_"
path_pcm = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\pcm_bible\c_"
for j, book in enumerate(two_chapters):
    output_path_en = path_en + str(j) + ".txt"
    output_path_pcm = path_pcm + str(j) + ".txt"
    for i in book:
        if i not in two_capters_problems:

            en_verse_path = en_path + str(i)
            en_counter = 0
            en_verse = ""
            with open(en_verse_path, "r") as fb:
                en_verse = fb.readlines()
            with open(output_path_en, "a") as fb:
                fb.writelines(en_verse)
            pcm_verse_path = pcm_path + i
            pcm_counter = 0
            pcm_verse = ""
            with open(pcm_verse_path, "r") as fb:
                pcm_verse = fb.readlines()
            with open(output_path_pcm, "a") as fb:
                fb.writelines(pcm_verse)
