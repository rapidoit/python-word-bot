class WordBot(object):
    def find_match(self, d_word, words=[]):
        matches = []
        max_distance = 3
        for _word in words:
            if len(_word) <= 0:
                continue
            will_add, candidate = self.edit_distance(_word, d_word, max_distance)
            if will_add:
                matches.append(candidate)
        return ', '.join(matches)

    def edit_distance(self, candidate, target, max_distance):
        longer, shorter = (target.lower(), candidate.lower()) \
            if len(target) > len(candidate) else (candidate.lower(), target.lower())
        weight = pow(2, len([c for c in longer if c not in ('a', 'e', 'i', 'o', 'u')]))
        prev_distance, distances = 0, range(len(longer) + 1)
        for short_index, short_char in enumerate(shorter):
            distances_ = [short_index + 1]
            min_index = 0
            current_distance = 99999999
            for long_index, long_char in enumerate(longer):
                if long_char == short_char:
                    value = distances[long_index]
                    distances_.append(value)
                else:
                    value = 1 + min((distances[long_index], distances[long_index + 1], distances_[-1]))
                    distances_.append(value)
                if value <= current_distance:
                    min_index = long_index
                    current_distance = value
            distances = distances_
            try:
                long_comp_char = longer[min_index]
                short_comp_char = short_char
                condition1 = current_distance <= max_distance
                condition2 = prev_distance == current_distance
                condition3 = long_comp_char == short_comp_char
                condition4 = short_comp_char not in ('a', 'e', 'i', 'o', 'u')
                if condition1 and ((condition2 and condition4) or condition3):
                    weight = weight / 2
                elif not (condition4 and condition3 and condition2):
                    weight = weight * 2
                prev_distance = current_distance
            except Exception as exp:
                print(exp)
        return (weight * distances[-1]) <= 1, candidate


print(WordBot().find_match('Badda', ['Nadda', 'Norda', 'Bodda', 'Badaa']))

# Output: Nadda, Bodda, Badaa
