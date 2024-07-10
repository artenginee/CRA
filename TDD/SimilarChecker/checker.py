class SimilarChecker:
    def similar_cnt_point(self, shorter, longer):
        if len(shorter) > len(longer):
            return self.similar_cnt_point(longer, shorter)

        if self.is_same_length(shorter, longer):
            return 60
        if self.is_more_than_twice(shorter, longer):
            return 0

        gap = len(longer) - len(shorter)
        return 60 - (gap) * 60 // len(shorter)

    def is_more_than_twice(self, a, b):
        return len(a) * 2 <= len(b)

    def is_same_length(self, a, b):
        return len(a) == len(b)
