data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

algo = data[0]
algo = ['0' if ch == '.' else '1' for ch in algo]

image = []
for i in range(2, len(data)):
    ln = data[i]
    if not ln.strip(): continue

    ln = ['0' if ch == '.' else '1' for ch in ln]
    image.append(list(ln))

tick = algo[0] == '0'

# expand
def expand(amount):
    pad = algo[-1] if not tick else algo[0]

    L = len(image[0])+amount*2
    for i,ln in enumerate(image):
        image[i] = [pad]*amount + ln + [pad]*amount
    for _ in range(amount):
        image.insert(0, [pad]*L)
    for _ in range(amount):
        image.append([pad]*L)

def get_ln_bit(start, end, y):
    pad = algo[-1] if not tick else algo[0]
    if y < 0: return pad*3
    elif y >= len(image): return pad*3
    L = len(image[0])
    ln = ''
    if start < 0: ln = pad
    ln += ''.join(image[y][max(0,start):min(end,L)])
    if end > L: ln += pad
    return ln

def calculate():
    global tick
    temp = {}
    W = len(image[0])
    H = len(image)
    for y in range(H):
        for x in range(W):
            combined = ''
            for a in range(y-1, y+2):
                combined += get_ln_bit(x-1, x+2, a)
            bin_num = int(combined, 2)
            pixel = algo[bin_num]
            temp[(x,y)] = pixel

    for k in temp:
        image[k[1]][k[0]] = temp[k]

    if algo[0] == '1':
        tick = not tick


def print_img():
    for ln in image:
        print(''.join(['#' if ch == '1' else '.' for ch in ln]))

expand(1)
calculate()
print_img()
expand(1)
calculate()
print_img()
cnt = 0
for r in image:
    for ch in r:
        if ch == '1': cnt += 1

print(cnt)
