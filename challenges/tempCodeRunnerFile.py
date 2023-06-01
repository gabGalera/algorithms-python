rmanence_period[index][0] or not permanence_period[index][1]:
            return None
        if type(permanence_period[index][0]) is str:
            if not permanence_period[index][0].isdigit():
                return None
        if type(permanence_period[index][1]) is str:
            if not permanence_period[index][1].isdigit():
                return Non