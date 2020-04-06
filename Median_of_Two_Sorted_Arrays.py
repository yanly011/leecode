class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        if ((l1 + l2) % 2 == 0):
            midPosition = int((l1 + l2) / 2 + 1)
            odd = False
        else:
            midPosition = int((l1 + l2 + 1) / 2)
            odd = True

        pos1 = 0
        pos2 = 0
        combined = []

        if (l1 == 1 and l2 == 1):
            return float(nums1[0] + nums2[0]) / 2

        if (l1 == 0 and l2 == 1):
            return nums2[0]

        if (l1 == 1 and l2 == 0):
            return nums1[0]

        if (l1 == 0 and l2 == 0):
            return 0.0
        else:
            if (l1 == 0 and l2 > 1):
                if (odd is True):
                    return nums2[midPosition - 1]
                else:
                    return (nums2[midPosition - 1] + nums2[midPosition - 2]) / 2
            elif (l2 == 0 and l1 > 1):
                if (odd is True):
                    return nums1[midPosition - 1]
                else:
                    return (nums1[midPosition - 1] + nums1[midPosition - 2]) / 2

        numInNums1 = nums1[pos1]
        numInNums2 = nums2[pos2]

        while (1):
            if (numInNums1 < numInNums2):
                combined.append(numInNums1)
                if (pos1 < (l1 - 1)):
                    pos1 = pos1 + 1
                    numInNums1 = nums1[pos1]
                else:
                    combined = combined + nums2[pos2:]
                    if (odd is True):
                        return combined[midPosition - 1]
                    else:
                        return (combined[midPosition - 1] + combined[midPosition - 2]) / 2

            elif (numInNums1 > numInNums2):
                combined.append(numInNums2)
                if (pos2 < (l2 - 1)):
                    pos2 = pos2 + 1
                    numInNums2 = nums2[pos2]
                else:
                    combined = combined + nums1[pos1:]
                    if (odd is True):
                        return combined[midPosition - 1]
                    else:
                        return (combined[midPosition - 1] + combined[midPosition - 2]) / 2

            else:
                if (numInNums1 == numInNums2):
                    combined.append(numInNums1)
                    if (pos1 < (l1 - 1)):
                        pos1 = pos1 + 1
                        numInNums1 = nums1[pos1]
                    else:
                        combined = combined + nums2[pos2:]
                        if (odd is True):
                            return combined[midPosition - 1]
                        else:
                            return (combined[midPosition - 1] + combined[midPosition - 2]) / 2
                    combined.append(numInNums2)
                    if (pos2 < (l2 - 1)):
                        pos2 = pos2 + 1
                        numInNums2 = nums2[pos2]
                    else:
                        combined = combined + nums1[pos1:]
                        if (odd is True):
                            return combined[midPosition - 1]
                        else:
                            return (combined[midPosition - 1] + combined[midPosition - 2]) / 2
            if (odd is True and len(combined) == midPosition):
                return float(combined[-1])
            elif (odd is False and len(combined) == midPosition):
                return (combined[-1] + combined[-2]) / 2

