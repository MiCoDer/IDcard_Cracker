import multiprocessing as mp
import readline
from itertools import product

locationCode = {
    'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,
    'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,
    'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33
}

weights = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]

def compute_checksum(full_digits):
    return sum(int(n) * w for n, w in zip(full_digits, weights)) % 10

def calculate_check_digit(pre_digits):
    base = sum(int(n) * w for n, w in zip(pre_digits, weights[:-1]))
    for d in '0123456789':
        if (base + int(d) * weights[-1]) % 10 == 0:
            return d
    return None

def process_combinations(args):
    ID_template, q_indices = args
    results = []
    non_digit = lambda c: not c.isdigit()

    
    digit_domains = []
    for idx in q_indices:
        if idx == 1:
            digit_domains.append(['1', '2'])  
        else:
            digit_domains.append([str(d) for d in range(10)])

    for digits in product(*digit_domains):
        chars = list(ID_template)
        for i, d in zip(q_indices, digits):
            chars[i] = d

        if chars[1] not in ('1', '2'):
            continue  

        if chars[0] not in locationCode:
            continue  

        letter_code = str(locationCode[chars[0]])
        numeric_part = list(letter_code) + chars[1:]
        if any(non_digit(c) for c in numeric_part):
            continue
        if compute_checksum(numeric_part) == 0:
            results.append(''.join(chars))
    return results

def solve(ID):
    if len(ID) != 10 or not ID[0].isalpha():
        raise ValueError("格式錯誤，第一碼必須是英文字母")

    chars = list(ID.upper())
    q_indices = [i for i, c in enumerate(chars) if c == '?']
    total_q = len(q_indices)

    letter_code = str(locationCode[chars[0]])

    
    if total_q == 1 and q_indices[0] == 9:
        if chars[1] not in ('1', '2'):
            return []
        digits = list(letter_code) + chars[1:9]
        if any(not c.isdigit() for c in digits):
            return []
        check_digit = calculate_check_digit(digits)
        if check_digit:
            chars[9] = check_digit
            full = list(letter_code) + chars[1:]
            if compute_checksum(full) == 0:
                return [''.join(chars)]
        return []

    
    cpu_count = mp.cpu_count()
    chunk_count = cpu_count * 2
    task_args = [(chars.copy(), q_indices)] * chunk_count

    with mp.Pool(processes=cpu_count) as pool:
        results = pool.map(process_combinations, task_args)

    return list(set(r for group in results for r in group))

if __name__ == "__main__":
    try:
        ID = input("輸入身份證（如 A12345??8?）: ").strip().upper()

        if not ID or len(ID) != 10 or not ID[0].isalpha():
            raise ValueError("錯誤：身份證格式不正確，第一碼需為英文字母，總長 10 碼")

        results = solve(ID)
        count = len(results)

        if count == 0:
            print("\n沒有找到有效身份證")
        elif count > 100:
            print(f"\n⚠ 找到 {count} 筆合法組合。")
            show = input("是否要顯示全部結果？(y/n): ").strip().lower()
            if show.startswith('y'):
                for r in results:
                    print(r)
        else:
            for r in results:
                print(r)

        print(f"\n總共找到 {count} 種可能")

    except Exception as e:
        print(f"錯誤：{e}")
