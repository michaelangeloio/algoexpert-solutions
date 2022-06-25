def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    sum = 0
    redLen = len(redShirtSpeeds)
    blueLen = len(blueShirtSpeeds)
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=True if fastest else False)
    for i in range(redLen):
        sum += redShirtSpeeds[i] if redShirtSpeeds[i] >= blueShirtSpeeds[i] else blueShirtSpeeds[i]
    return sum
