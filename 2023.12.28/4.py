from pprint import pprint
from pathlib import Path
import os
def search_context(word: str, *args: str, n_lines: int = 0) -> list[dict]:
    
    os.chdir('data')
    txt_list = list(Path('.').glob('*.txt'))
    words = (word, *args)
    lines_find = []
    for file in txt_list:
        with open(file, encoding='utf-8') as f:
            file_lines = [line.rstrip() for line in f.readlines()]
            for line in file_lines:
                for word in words:
                    if word.lower() in line.lower():
                        line_index = file_lines.index(line)
                        if line_index-n_lines<0:
                            lines_find.append({'keyword': word,
                                               'filename': file.name,
                                               'line': line_index+1,
                                               'context': n_lines,
                                               'text': file_lines[:line_index+n_lines+1]})
                        else:
                            lines_find.append({'keyword': word,
                                               'filename': file.name,
                                               'line': line_index+1,
                                               'context': n_lines,
                                               'text': file_lines[line_index-n_lines:line_index+n_lines+1]})
    return lines_find

# >>> pprint(search_context('Девушка', 'мундир', n_lines=1))
# [{'context': 1,
  # 'filename': 'E3ln1.txt',
  # 'keyword': 'мундир',
  # 'line': 19,
  # 'text': ['Дом господский стоял одиночкой на юру, то есть на возвышении, '
           # 'открытом всем ветрам, какие только вздумается подуть; покатость '
           # 'горы, на которой он стоял, была одета подстриженным дерном. На ней '
           # 'были разбросаны по-английски две-три клумбы с кустами сиреней и '
           # 'желтых акаций; пять-шесть берез небольшими купами кое-где '
           # 'возносили свои мелколистные жиденькие вершины. Под двумя из них '
           # 'видна была беседка с плоским зеленым куполом, деревянными голубыми '
           # 'колоннами и надписью: «Храм уединенного размышления»; пониже пруд, '
           # 'покрытый зеленью, что, впрочем, не в диковинку в аглицких садах '
           # 'русских помещиков. У подошвы этого возвышения, и частию по самому '
           # 'скату, темнели вдоль и поперек серенькие бревенчатые избы, которые '
           # 'герой наш, неизвестно по каким причинам, в ту ж минуту принялся '
           # 'считать и насчитал более двухсот; нигде между ними растущего '
           # 'деревца или какой-нибудь зелени; везде глядело только одно бревно.',
           # 'Вид оживляли две бабы, которые, картинно подобравши платья и '
           # 'подтыкавшись со всех сторон, брели по колени в пруде, влача за два '
           # 'деревянные кляча изорванный бредень, где видны были два '
           # 'запутавшиеся рака и блестела попавшаяся плотва; бабы, казались, '
           # 'были между собою в ссоре и за что-то перебранивались. Поодаль в '
           # 'стороне темнел каким-то скучно-синеватым цветом сосновый лес. Даже '
           # 'самая погода весьма кстати прислужилась: день был не то ясный, не '
           # 'то мрачный, а какого-то светло-серого цвета, какой бывает только '
           # 'на старых мундирах гарнизонных солдат, этого, впрочем, мирного '
           # 'войска, но отчасти нетрезвого по воскресным дням. Для пополнения '
           # 'картины не было недостатка в петухе, предвозвестнике переменчивой '
           # 'погоды, который, несмотря на то что голова продолблена была до '
           # 'самого мозгу носами других петухов по известным делам волокитства, '
           # 'горланил очень громко и даже похлопывал крыльями, обдерганными, '
           # 'как старые рогожки.',
           # 'Подъезжая ко двору, Чичиков заметил на крыльце самого хозяина, '
           # 'который стоял в зеленом шалоновом сюртуке, приставив руку ко лбу в '
           # 'виде зонтика над глазами, чтобы рассмотреть получше подъезжавший '
           # 'экипаж. По мере того как бричка близилась к крыльцу, глаза его '
           # 'делались веселее и улыбка раздвигалась более и более.']},
 # {'context': 1,
  # 'filename': 'le1UO.txt',
  # 'keyword': 'Девушка',
  # 'line': 9,
  # 'text': [' - Вы, душенька, ошиблись, - сказала она, - эта записка не ко мне.',
           # ' - Нет, точно к вам! - отвечала смелая девушка, не скрывая лукавой '
           # 'улыбки. - Извольте прочитать!',
           # 'Германн трепетал, как тигр, ожидая назначенного времени. В десять '
           # 'часов вечера он уж стоял перед домом графини. Погода была ужасная: '
           # 'ветер выл, мокрый снег падал хлопьями; фонари светились тускло; '
           # 'улицы были пусты. Изредка тянулся Ванька на тощей кляче своей, '
           # 'высматривая запоздалого седока. Германн стоял в одном сертуке, не '
           # 'чувствуя ни ветра, ни снега. Наконец графинину карету подали. '
           # 'Германн видел, как лакеи вынесли под руки сгорбленную старуху, '
           # 'укутанную в соболью шубу, и как вослед за нею, в холодном плаще, с '
           # 'головой, убранною свежими цветами, мелькнула ее воспитанница. '
           # 'Дверцы захлопнулись. Карета тяжело покатилась по рыхлому снегу. '
           # 'Швейцар запер двери. Окна померкли. Германн стал ходить около '
           # 'опустевшего дома: он подошел к фонарю, взглянул на часы, - было '
           # 'двадцать минут двенадцатого. Он остался под фонарем, устремив '
           # 'глаза на часовую стрелку и выжидая остальные минуты. Ровно в '
           # 'половине двенадцатого Германн ступил на графинино крыльцо и взошел '
           # 'в ярко освещенные сени. Швейцара не было. Германн взбежал по '
           # 'лестнице, отворил двери в переднюю и увидел слугу, спящего под '
           # 'лампою, в старинных, запачканных креслах. Легким и твердым шагом '
           # 'Германн прошел мимо его. Зала и гостиная были темны. Лампа слабо '
           # 'освещала их из передней. Германн вошел в спальню. Перед кивотом, '
           # 'наполненным старинными образами, теплилась золотая лампада. '
           # 'Полинялые штофные кресла и диваны с пуховыми подушками, с сошедшей '
           # 'позолотою, стояли в печальной симметрии около стен, обитых '
           # 'китайскими обоями. На стене висели два портрета, писанные в Париже '
           # 'm-me Lebrun. Один из них изображал мужчину лет сорока, румяного и '
           # 'полного, в светло-зеленом мундире и со звездою; другой - молодую '
           # 'красавицу с орлиным носом, с зачесанными висками и с розою в '
           # 'пудреных волосах. По всем углам торчали фарфоровые пастушки, '
           # 'столовые часы работы славного Leroy, коробочки, рулетки, веера и '
           # 'разные дамские игрушки, изобретенные в конце минувшего столетия '
           # 'вместе с Монгольфьеровым шаром и Месмеровым магнетизмом. Германн '
           # 'пошел за ширмы. За ними стояла маленькая железная кровать; справа '
           # 'находилась дверь, ведущая в кабинет; слева, другая - в коридор. '
           # 'Германн ее отворил, увидел узкую, витую лестницу, которая вела в '
           # 'комнату бедной воспитанницы... Но он воротился и вошел в темный '
           # 'кабинет.']},
 # {'context': 1,
  # 'filename': 'le1UO.txt',
  # 'keyword': 'мундир',
  # 'line': 10,
  # 'text': [' - Нет, точно к вам! - отвечала смелая девушка, не скрывая лукавой '
           # 'улыбки. - Извольте прочитать!',
           # 'Германн трепетал, как тигр, ожидая назначенного времени. В десять '
           # 'часов вечера он уж стоял перед домом графини. Погода была ужасная: '
           # 'ветер выл, мокрый снег падал хлопьями; фонари светились тускло; '
           # 'улицы были пусты. Изредка тянулся Ванька на тощей кляче своей, '
           # 'высматривая запоздалого седока. Германн стоял в одном сертуке, не '
           # 'чувствуя ни ветра, ни снега. Наконец графинину карету подали. '
           # 'Германн видел, как лакеи вынесли под руки сгорбленную старуху, '
           # 'укутанную в соболью шубу, и как вослед за нею, в холодном плаще, с '
           # 'головой, убранною свежими цветами, мелькнула ее воспитанница. '
           # 'Дверцы захлопнулись. Карета тяжело покатилась по рыхлому снегу. '
           # 'Швейцар запер двери. Окна померкли. Германн стал ходить около '
           # 'опустевшего дома: он подошел к фонарю, взглянул на часы, - было '
           # 'двадцать минут двенадцатого. Он остался под фонарем, устремив '
           # 'глаза на часовую стрелку и выжидая остальные минуты. Ровно в '
           # 'половине двенадцатого Германн ступил на графинино крыльцо и взошел '
           # 'в ярко освещенные сени. Швейцара не было. Германн взбежал по '
           # 'лестнице, отворил двери в переднюю и увидел слугу, спящего под '
           # 'лампою, в старинных, запачканных креслах. Легким и твердым шагом '
           # 'Германн прошел мимо его. Зала и гостиная были темны. Лампа слабо '
           # 'освещала их из передней. Германн вошел в спальню. Перед кивотом, '
           # 'наполненным старинными образами, теплилась золотая лампада. '
           # 'Полинялые штофные кресла и диваны с пуховыми подушками, с сошедшей '
           # 'позолотою, стояли в печальной симметрии около стен, обитых '
           # 'китайскими обоями. На стене висели два портрета, писанные в Париже '
           # 'm-me Lebrun. Один из них изображал мужчину лет сорока, румяного и '
           # 'полного, в светло-зеленом мундире и со звездою; другой - молодую '
           # 'красавицу с орлиным носом, с зачесанными висками и с розою в '
           # 'пудреных волосах. По всем углам торчали фарфоровые пастушки, '
           # 'столовые часы работы славного Leroy, коробочки, рулетки, веера и '
           # 'разные дамские игрушки, изобретенные в конце минувшего столетия '
           # 'вместе с Монгольфьеровым шаром и Месмеровым магнетизмом. Германн '
           # 'пошел за ширмы. За ними стояла маленькая железная кровать; справа '
           # 'находилась дверь, ведущая в кабинет; слева, другая - в коридор. '
           # 'Германн ее отворил, увидел узкую, витую лестницу, которая вела в '
           # 'комнату бедной воспитанницы... Но он воротился и вошел в темный '
           # 'кабинет.',
           # 'Время шло медленно. Все было тихо. В гостиной пробило двенадцать; '
           # 'по всем комнатам часы одни за другими прозвонили двенадцать, - все '
           # 'умолкло опять. Германн стоял, прислонясь к холодной печке. Он был '
           # 'спокоен; сердце его билось ровно, как у человека, решившегося на '
           # 'что-нибудь опасное, но необходимое. Часы пробили первый и второй '
           # 'час утра, - и он услышал дальний стук кареты. Невольное волнение '
           # 'овладело им. Карета подъехала и остановилась. Он услышал стук '
           # 'опускаемой подножки. В доме засуетились. Люди побежали, раздались '
           # 'голоса, и дом осветился. В спальню вбежали три старые горничные, и '
           # 'графиня, чуть живая, вошла и опустилась в вольтеровы кресла. '
           # 'Германн глядел в щелку: Лизавета Ивановна прошла мимо его. Германн '
           # 'услышал ее торопливые шаги по ступеням ее лестницы. В сердце его '
           # 'отозвалось нечто похожее на угрызение совести и снова умолкло. Он '
           # 'окаменел.']},
 # {'context': 1,
  # 'filename': 'r62Bf.txt',
  # 'keyword': 'Девушка',
  # 'line': 23,
  # 'text': ['Ему уже много раз случалось проходить, например, домой и '
           # 'совершенно не помнить дороги, по которой он шел, и он уже привык '
           # 'так ходить. Но в идущей женщине было что-то такое странное и с '
           # 'первого же взгляда бросающееся в глаза, что мало-помалу внимание '
           # 'его начало к ней приковываться, - сначала нехотя и как бы с '
           # 'досадой, а потом все крепче и крепче. Ему вдруг захотелось понять, '
           # 'что именно в этой женщине такого странного?',
           # 'Во-первых, она, должно быть, девушка очень молоденькая, шла по '
           # 'такому зною простоволосая, без зонтика и без перчаток, как-то '
           # 'смешно размахивая руками. На ней было шелковое, из легкой материи '
           # '(«матерчатое») платьице, но тоже как-то очень чудно надетое, едва '
           # 'застегнутое, и сзади у талии, в самом начале юбки, разорванное; '
           # 'целый клок отставал и висел болтаясь. Маленькая косыночка была '
           # 'накинута на обнаженную шею, но торчала как-то криво и боком. К '
           # 'довершению, девушка шла нетвердо, спотыкаясь и даже шатаясь во все '
           # 'стороны.',
           # 'Эта встреча возбудила, наконец, все внимание Раскольникова. Он '
           # 'сошелся с девушкой у самой скамейки, но, дойдя до скамьи, она так '
           # 'и повалилась на нее, в угол, закинула на спинку скамейки голову и '
           # 'закрыла глаза, по-видимому, от чрезвычайного утомления. '
           # 'Вглядевшись в нее, он тотчас же догадался, что она совсем была '
           # 'пьяна. Странно и дико было смотреть на такое явление. Он даже '
           # 'подумал, не ошибается ли он.']},
 # {'context': 1,
  # 'filename': 'r62Bf.txt',
  # 'keyword': 'Девушка',
  # 'line': 25,
  # 'text': ['Эта встреча возбудила, наконец, все внимание Раскольникова. Он '
           # 'сошелся с девушкой у самой скамейки, но, дойдя до скамьи, она так '
           # 'и повалилась на нее, в угол, закинула на спинку скамейки голову и '
           # 'закрыла глаза, по-видимому, от чрезвычайного утомления. '
           # 'Вглядевшись в нее, он тотчас же догадался, что она совсем была '
           # 'пьяна. Странно и дико было смотреть на такое явление. Он даже '
           # 'подумал, не ошибается ли он.',
           # 'Пред ним было чрезвычайно молоденькое личико, лет шестнадцати, '
           # 'даже, может быть, только пятнадцати, - маленькое, белокуренькое, '
           # 'хорошенькое, но все разгоревшееся и как будто припухшее. Девушка, '
           # 'кажется, очень мало уж понимала; одну ногу заложила за другую, '
           # 'причем выставила ее гораздо больше, чем следовало, и, по всем '
           # 'признакам, очень плохо сознавала, что она на улице.',
           # 'Раскольников не сел и уйти не хотел, а стоял перед нею в '
           # 'недоумении. Этот бульвар и всегда стоит пустынный, теперь же, во '
           # 'втором часу и в такой зной, никого почти не было. И, однако ж, в '
           # 'стороне, шагах в пятнадцати, на краю бульвара, остановился один '
           # 'господин, которому, по всему видно было, очень бы хотелось тоже '
           # 'подойти к девочке с какими-то целями. Он тоже, вероятно, увидел ее '
           # 'издали и догонял, но ему помешал Раскольников. Он бросал на него '
           # 'злобные взгляды, стараясь, впрочем, чтобы тот их не заметил, и '
           # 'нетерпеливо ожидал своей очереди, когда досадный оборванец уйдет. '
           # 'Дело было понятное. Господин этот был лет тридцати, плотный, '
           # 'жирный, кровь с молоком, с розовыми губами и с усиками и очень '
           # 'щеголевато одетый. Раскольников ужасно разозлился; ему вдруг '
           # 'захотелось как-нибудь оскорбить этого жирного франта. Он на минуту '
           # 'оставил девочку и подошел к господину.']},
 # {'context': 1,
  # 'filename': 'r62Bf.txt',
  # 'keyword': 'Девушка',
  # 'line': 38,
  # 'text': ['Городовой мигом все понял и сообразил. Толстый господин был, '
           # 'конечно, понятен, оставалась девочка. Служивый нагнулся над нею '
           # 'разглядеть поближе, и искреннее сострадание изобразилось в его '
           # 'чертах.',
           # ' - Ax, жаль-то как! - сказал он, качая головой, - совсем еще как '
           # 'ребенок. Обманули, это как раз. Послушайте, сударыня, - начал он '
           # 'звать ее, - где изволите проживать? - Девушка открыла усталые и '
           # 'посоловелые глаза, тупо посмотрела на допрашивающих и отмахнулась '
           # 'рукой.',
           # ' - Послушайте, - сказал Раскольников, - вот (он пошарил в кармане '
           # 'и вытащил двадцать копеек; нашлись), вот, возьмите извозчика и '
           # 'велите ему доставить по адресу. Только бы адрес-то нам узнать!']}]