class WordBot(object):
    def find_match(self, d_word, words=[]):
        weight, distance = 99999999, 99999999
        for _word in words:
            if len(_word) <= 0:
                continue
            t, a, w, d = self.edit_distance(_word, d_word, 2)
            if (d <= 2 and w <= 10) or w <= 1:
                if w < weight and d < distance:
                    weight = w
                    distance = d

    def edit_distance(self, candidate, target, max_distance):
        longer, shorter = target.lower(), candidate.lower() \
            if len(target) > len(candidate) else candidate.lower(), target.lower()
        weight = pow(10, len([c for c in longer if c not in ('a', 'e', 'i', 'o', 'u')]))
        prev_distance, distances = 0, range(len(longer) + 1)
        for i2, c2 in enumerate(word2):
            distances_ = [i2 + 1]
            min_index = 0
            current_distance = 99999999
            for i1, c1 in enumerate(word1):
                if c1 == c2:
                    val = distances[i1]
                    distances_.append(val)
                else:
                    val = 1 + min((distances[i1], distances[i1 + 1], distances_[-1]))
                    distances_.append(val)
                if val <= current_distance:
                    min_index = i1
                    current_distance = val
            distances = distances_
            try:
                s1c = word1[min_index]
                s2c = c2
                condition1 = current_distance <= maximum_distance
                condition2 = prev_distance == current_distance
                condition3 = s1c == s2c
                condition4 = s2c not in ('a', 'e', 'i', 'o', 'u')
                if condition1 and ((condition2 and condition4) or condition3):
                    weight = weight / 10
                elif not (condition4 and condition3 and condition2):
                    weight = weight * 10
                prev_distance = current_distance
            except Exception as exp:
                print(exp)
        return word1, word2, weight, distances[-1]
