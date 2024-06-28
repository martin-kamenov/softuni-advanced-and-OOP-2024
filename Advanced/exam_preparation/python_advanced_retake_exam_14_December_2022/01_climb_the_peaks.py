from collections import deque

food_portions = [int(x) for x in input().split(', ')]
stamina = deque([int(x) for x in input().split(', ')])
conquered_peaks = []

peaks = {
    80: 'Vihren',
    90: 'Kutelo',
    100: 'Banski Suhodol',
    60: 'Polezhan',
    70: 'Kamenitza',
}

for peak in peaks:

    while food_portions and stamina:
        food = food_portions.pop()
        daily_stamina = stamina.popleft()

        result = food + daily_stamina

        if result >= peak:
            conquered_peaks.append(peaks[peak])
            break

    if not food_portions and not stamina:
        break

if len(conquered_peaks) == len(peaks):
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if conquered_peaks:
    print('Conquered peaks:')
    print('\n'.join(conquered_peaks))
