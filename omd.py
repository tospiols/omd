def step1():
    print(
        'Утка-маляр решила зайти выпить в бар. '
        'Взять ей зонтик ☂️?'
    )
    option = ''
    options_rain = {'да': True, 'нет': False}
    while option not in options_rain:
        print('Выберите: {}/{}'.format(*options_rain))
        option = input()

    if options_rain[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Уточка просто любила красить всё в свою любимую комбинацию '
          'цветов и поэтому решила стать маляром. Как '
          'только она вышла на улицу, начался дождь. Уточке он'
          ' был не страшен, ведь её лапки не мокнут, '
          'а ещё она взяла с собой зонт. Уточка стала думать,'
          ' в какой бар ей пойти, в любимый или в тот, который'
          ' поближе?')
    option = ''
    options_bar = {'любимый': True, 'поближе': False}
    while option not in options_bar:
        print('Выберите: {}/{}'.format(*options_bar))
        option = input()

    if options_bar[option]:
        return step3_far()
    return step3_close()


def step2_no_umbrella():
    print('Как только уточка вышла на улицу, начался дождь.'
          ' Это не удивительно, ведь погода в Петербурге не сказка.'
          ' Возможно, если бы она жила в Москве, всё было бы'
          ' по-другому. А сейчас уточка идет в бар неподалёку.')
    return step3_close()


beers = False
beers_counter = 0


def step3_close():
    global beers, beers_counter
    print('Уточка на то и уточка, чтобы не мокнуть быстро. Когда'
          ' она пришла в бар, она была почти сухой. Ничто не'
          ' предещало беды и уточка решила заказать пиво. К сожалению,'
          ' её любимое пиво кончилось и пришлось выбирать '
          'между кофейным стаутом и вишневым криком')
    option = ''
    options_close_bar = {'кофейный стаут': True, 'вишневый крик': False}
    while option not in options_close_bar:
        print('Выберите: {}/{}'.format(*options_close_bar))
        option = input()
    if options_close_bar[option]:
        return step4_home()
    beers_counter += 1
    beers = True
    return step3_return()


def step3_return():
    print('Уточке не понравилось выпитое пиво, но захотелось'
          ' выпить ещё. Уточка решила, что она может и доплыть до'
          'своего любимого бара (она же уточка!),'
          ' но попить своего любимого пива.')
    input('Поддержите уточку:')
    print('Пока уточка шла к своему любимому бару, она задумалась'
          ' о своей жизни. Свинцовые тучи Петербурга угнетали'
          ' её, она хотела сделать город светлее, но её любимую'
          ' комбинацию цветов запретили на территории России.'
          ' Оставалось только выпить её любимое пиво.')
    return step3_far()


def step3_far():
    global beers_counter
    print('Пока уточка дошла до своего любимого бара, начало '
          'темнеть. В её любимом баре, уточка решила заказать своё '
          'любимое пиво, лаймовый сауэр. Возможно, это странный '
          'выбор для уточки, но и уточка не самая обычная.')
    option = ''
    options_far_bar = {'выпить ещё': True, 'уйти': False}
    while option not in options_far_bar:
        print('Выберите: {}/{}'.format(*options_far_bar))
        option = input()
    if options_far_bar[option]:
        beers_counter += 1
        return step5_1more()
    return step5_finish()


def step5_1more():
    global beers_counter
    print(f'Уточка выпила уже {beers_counter} стакана пива. '
          f'Она знала, что после четвертого пива ей станет плохо,'
          f' но нужно было решить, хочет ли она ещё одно?')
    option = ''
    options_far_bar = {'выпить ещё': True, 'уйти': False}
    while option not in options_far_bar:
        print('Выберите: {}/{}'.format(*options_far_bar))
        option = input()
    if options_far_bar[option]:
        beers_counter += 1
        return step5_1more()
    if beers_counter > 3:
        return step6_late()
    return step5_finish()


def step6_late():
    print('Уточка явно перебрала и отправилась домой. А ведь '
          'сегодня был дедлайн по проекту, который она должна была'
          ' доделать. Теперь она может только винить себя '
          'в том, что она неисправима.')


def step4_home():
    print('Это был ещё один день, когда уточка не смогла показать'
          ' себя миру. Она чувствовала, что надо что-то менять,'
          'но не знала что именно.')


def step5_finish():
    print('Когда уточка вышла из бара, было ещё не поздно. На'
          ' улице была ярчайшая радуга, а уточка была в отличном '
          'расположении духа. Она решила открыться миру. Пусть'
          ' у самой необычной уточки Петербурга всё получится.')


if __name__ == '__main__':
    step1()
