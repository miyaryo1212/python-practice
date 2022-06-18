import math

print(f'{"π: "}{str(math.pi)}')
print(f'{"弧度法 → 度数法の変換: "}{str(math.pi)}{" → "}{str(math.degrees(math.pi))}')
print(f'{"度数法 → 弧度法の変換: "}{"180.0"}{" → "}{str(math.radians(180))}')
sin30 = math.sin(math.radians(30))
print(f'{"sin 30°: "}{str(sin30)}')
