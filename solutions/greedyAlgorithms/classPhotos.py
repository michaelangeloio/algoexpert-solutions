def classPhotos(redShirtHeights, blueShirtHeights):
    redMax = max(redShirtHeights)
    blueMax = max(blueShirtHeights)
    backRow = []
    frontRow = []
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    if redMax == blueMax:
        return False
    elif redMax > blueMax:
        backRow = backRow + redShirtHeights
        frontRow = frontRow + blueShirtHeights
    else:
        backRow = backRow + blueShirtHeights
        frontRow = frontRow + redShirtHeights
    for i, val in enumerate(backRow):
        if val <= frontRow[i]:
            return False
    return True
    
