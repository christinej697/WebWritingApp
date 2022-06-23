from django import forms

class DLR1_1Form(forms.Form):
    OPTIONS = (
        ("a", "Power is energy per unit time."),
        ("b", "The voltage source supplies power in the above circuit."),
        ("c", "The resistors dissipate power in the above circuit."),
        ("d", "The total amount of power dissipated by the three resistors must precisely equal the amount of power provided by the source."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS,required=False)

class DLR2_1Form(forms.Form):
    OPTIONS = (
        ("a", "The voltage source provides energy and the resistor dissipates energy."),
        ("b", "The voltage source is best considered a source of constant current."),
        ("c", "The voltage source is best considered a source of constant power."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS,required=False)

class DLR3_1Form(forms.Form):
    OPTIONS = (
        ("a", 'Since I\N{Latin Subscript Small Letter X} comes after resistor R\N{Latin Subscript Small Letter X} and I\N{Greek Subscript Small Letter Gamma} comes after both R\N{Latin Subscript Small Letter X} and R\N{Greek Subscript Small Letter Gamma}, I\N{Latin Subscript Small Letter S}>I\N{Latin Subscript Small Letter X}>I\N{Greek Subscript Small Letter Gamma}.'),
        ("b", 'I\N{Latin Subscript Small Letter S}=I\N{Latin Subscript Small Letter X}=\N{Greek Subscript Small Letter Gamma}.'),
        ("c", "Neither of the above is true."),
    )
    choice = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)

class DLR3_2Form(forms.Form):
    OPTIONS = (
        ("a", "Since R\N{Latin Subscript Small Letter X} comes before R\N{Greek Subscript Small Letter Gamma}, R\N{Latin Subscript Small Letter X} will require more potential difference than does R\N{Greek Subscript Small Letter Gamma}."),
        ("b", 'The overall resistance in the circuit has decreased and so neither resistor needs as much potential difference.'),
        ("c", "The current in the circuit will increase."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS,required=False)

class DLR4_1Form(forms.Form):
    OPTIONS = (
        ("a", "R\N{SUBSCRIPT TWO} is less resistive but the potential difference across R\N{SUBSCRIPT TWO} has to be the same and so the current in R\N{SUBSCRIPT TWO} increases."),
        ("b", "Because the voltage drop across R\N{SUBSCRIPT TWO} must stay the same, as the resistance of R\N{SUBSCRIPT TWO} decreases, the current in resistor 2 must increase."),
        ("c", "Because the voltage drop across R\N{SUBSCRIPT THREE} remains the same and its value of resistance remains constant, so does the current in R\N{SUBSCRIPT THREE}."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS,required=False)

class DLR4_2Form(forms.Form):
    OPTIONS = (
        ("a", "Application of KVL has validated our arguments in Points 1-4."),
        ("b", "Application of KVL has demonstrated that there is a conflict arising from our arguments in Points 1-4."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS,required=False)

class DLR5_1Form(forms.Form):
    OPTIONS = (
        ("a", "Resistors D and E are tied together at one node."),
        ("b", "Resistors D and E are in series."),
        ("c", "Resistors D and F are tied together at one node."),
        ("d", "Resistors D and F are in series."),
        ("e", "Resistors D and G are tied together at one node."),
        ("f", "Resistors D and G are in series."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS,required=False)

class DLR7_1Form(forms.Form):
    OPTIONS = (
        ("a", "The voltage source provides energy to the circuit in question."),
        ("b", "Due to conservation of energy, the amount of energy supplied by the voltage source will not change as the resistance of R\N{SUBSCRIPT TWO} changes."),
        ("c", "The resistors in the circuit provide energy."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS,required=False)