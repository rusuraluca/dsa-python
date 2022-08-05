"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/course-schedule-iii/
"""
import heapq


class Solution:
    def scheduleCourse(self, courses) -> int:
        # sort primarily by last date
        # and secondarily by duration to sequentially iterate over courses
        courses.sort(key=lambda x: (x[1], x[0]))

        # past is the max heap of durations of courses that we have taken
        # and curr_time is the current time we are at
        past, curr_time = [], 0

        for duration, last_day in courses:
            if curr_time + duration <= last_day:
                # if we can incorporate this course in the current state then do so
                heappush(past, -duration);

                # update the curr_time variable
                curr_time += duration


            # if replacing longest course with current course can save some time
            else:
                # if past is not empty
                if past:
                    # longest course done so far
                    longest_course = -past[0]

                    # check if that course was longer than the current one
                    if longest_course > duration:
                        # removing longest_course and adding current course
                        # keeps number of courses same but reduces the curr_time
                        heappop(past)

                        # add current course to past
                        heappush(past, -duration)

                        # update curr_time
                        curr_time += duration - longest_course

        return len(past)