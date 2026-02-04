class Solution:
    def convertTemperature(self, Celsius):
        kel = Celsius + 273.15
        fhr = Celsius * 1.80 + 32.00
        kel = float(f"{kel:.5f}")
        fhr = float(f"{fhr:.5f}")
        return [kel , fhr]
    
s = Solution()
print(s.convertTemperature(32))
