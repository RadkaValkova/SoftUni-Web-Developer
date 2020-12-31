def is_winning(half1,half2, ch):
    if ch in half1 and ch in half2:
        first_count = half1.count(ch)
        second_count = half2.count(ch)
        if first_count == second_count and first_count >=6 and second_count >= 6:
            return True
        return False

        
def is_jackpot(half1,half2, ch):
    if ch in half1 and ch in half2:
        first_count = half1.count(ch)
        second_count = half2.count(ch)
        if first_count == 10 and second_count == 10:
            return True
        return False


text = input()
text = text.replace(' ', '')
text = text.split(',')

winning_tickets = []

for el in text:
    if len(el) == 20:
        first_half = el[:10]
        second_half = el[10:]
        if '@' in el or '#' in el or '$' in el or '^' in el:
            if '@' in el:
                if is_winning(first_half,second_half,'@'):
                    if is_jackpot(first_half,second_half,'@'):
                        print(f'ticket "{el}" - {10}{"@"} Jackpot!')
                    else:
                        print(f'ticket "{el}" - {second_half.count("@")}{"@"}')
                else:
                    print(f'ticket "{el}" - no match')
            elif '$' in el:
                if is_winning(first_half,second_half,'$'):
                    if is_jackpot(first_half,second_half,'$'):
                        print(f'ticket "{el}" - {10}{"$"} Jackpot!')
                    else:
                        print(f'ticket "{el}" - {second_half.count("$")}{"$"}')
                else:
                    print(f'ticket "{el}" - no match')
            elif '#' in el:
                if is_winning(first_half,second_half,'#'):
                    if is_jackpot(first_half,second_half,'#'):
                        print(f'ticket "{el}" - {10}{"#"} Jackpot!')
                    else:
                        print(f'ticket "{el}" - {second_half.count("#")}{"#"}')
                else:
                    print(f'ticket "{el}" - no match')
            elif '^' in el:
                if is_winning(first_half,second_half,'^'):
                    if is_jackpot(first_half,second_half,'^'):
                        print(f'ticket "{el}" - {10}{"^"} Jackpot!')
                    else:
                        print(f'ticket "{el}" - {second_half.count("^")}{"^"}')
                else:
                    print(f'ticket "{el}" - no match')

        else:
            print(f'ticket "{el}" - no match')
    else:
        print('invalid ticket')
