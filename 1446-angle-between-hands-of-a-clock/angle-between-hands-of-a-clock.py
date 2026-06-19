class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Calculate the angle of the hour hand
        hour_angle = 0.5 * (hour * 60 + minutes)
        
        # Calculate the angle of the minute hand
        minute_angle = 6 * minutes
        
        # Calculate the absolute difference between the two angles
        angle = abs(hour_angle - minute_angle)
        
        # Return the smaller angle
        if angle > 180:
            angle = 360 - angle
        return angle