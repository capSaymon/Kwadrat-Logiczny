import spacy
import re

class SentenceChecker():
    def __init__(self, question, outcome):
        self.nlp = spacy.load("pl_core_news_sm")
        self.question = question
        self.outcome = outcome

    
    def test_response_format(self):    
        assert "E:" in self.outcome
        assert "I:" in self.outcome
        assert "O:" in self.outcome

        linie = self.outcome.splitlines()
        assert len(linie) == 4


    def extract_sentence(self, response: str, apex: str) -> str:
        for line in response.splitlines():
            if f"{apex}:" in line:
                parts = line.split(":", 1)
                if len(parts) == 2:
                    return parts[1].strip()
        raise ValueError(f"No sentence type found: {apex}")


    def test_relation_between_sentences(self) -> bool:
        apex_a = self.extract_sentence(self.question, "A")
        apex_o = self.extract_sentence(self.outcome, "O")
        apex_i = self.extract_sentence(self.outcome, "I")
        apex_e = self.extract_sentence(self.outcome, "E")

        return (self.contradicts_a_o(apex_a, apex_o) and self.contradicts_i_e(apex_i, apex_e))


    def lemmatize(self, text: str) -> str:
        doc = self.nlp(text)
        return " ".join([token.lemma_ for token in doc])

    def normalize(self, text: str) -> str:
        return self.lemmatize(text.strip().lower().rstrip("."))

    def contradicts_a_o(self, sentence_a: str, sentence_o: str) -> bool:
        pattern_a = r"Wszystkie (.+?)"
        pattern_o = r"Niektóre (.+?) nie (.+?)"

        match_a = re.match(pattern_a, sentence_a.strip())
        match_o = re.match(pattern_o, sentence_o.strip())

        if match_a and match_o:
            a_full = self.normalize(match_a.group(1))
            subject_o = self.normalize(match_o.group(1))
            predicate_o = self.normalize(match_o.group(2))

            return f"{subject_o} {predicate_o}" in a_full or a_full in f"{subject_o} {predicate_o}"

        return False


    def contradicts_i_e(self, sentence_i: str, sentence_e: str) -> bool:
        pattern_i = r"Niektóre (.+?)"
        pattern_e = r"Żaden (.+?) nie (.+?)"

        match_i = re.match(pattern_i, sentence_i.strip())
        match_e = re.match(pattern_e, sentence_e.strip())

        if match_e is None:
            pattern_e = r"Żadna (.+?) nie (.+?)"
            match_e = re.match(pattern_e, sentence_e.strip())

        if match_i and match_e:
            i_full = self.normalize(match_i.group(1))
            subject_e = self.normalize(match_e.group(1))
            predicate_e = self.normalize(match_e.group(2))

            return f"{subject_e} {predicate_e}" in i_full or i_full in f"{subject_e} {predicate_e}"

        return False