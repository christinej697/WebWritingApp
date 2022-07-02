from django import forms
from exercises.models import StudentsDb

CONFIDENCE_CHOICES = [
    ('5','I am completely confident'),
    ('4', 'I am quite confident'),
    ('3', 'I am somewhat confident'),
    ('2', 'I have little confidence'),
    ('1', 'I am not at all confident'),
]

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
        ("b", 'The overall resistance in the circuit has decreased and so neither resistor will have as much potential difference.'),
        ("c", "The current in the circuit will increase."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS,required=False)

class DLR3_2bForm(forms.Form):
    OPTIONS = (
        ("a", "Since R\N{Latin Subscript Small Letter X} comes before R\N{Greek Subscript Small Letter Gamma}, R\N{Latin Subscript Small Letter X} will require more potential difference than does R\N{Greek Subscript Small Letter Gamma}."),
        ("b", 'The overall resistance in the circuit has decreased and so neither resistor will have as much potential difference.'),
        ("c", "The current in the circuit will increase."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS,required=False)
    seq_current_relationship = forms.CharField(widget=forms.Textarea, required=True)

class DLR4_1Form(forms.Form):
    OPTIONS = (
        ("a", "Because the voltage drop across R\N{SUBSCRIPT TWO} must stay the same, as the resistance of R\N{SUBSCRIPT TWO} decreases, the current in resistor 2 must increase."),
        ("b", "Because the voltage drop across R\N{SUBSCRIPT THREE} remains the same and its value of resistance remains constant, so does the current in R\N{SUBSCRIPT THREE}."),
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
    
class DLR8_1Form(forms.Form):
    OPTIONS = (
        ("a", "Elements in series share the same current."),
        ("b", "Elements in series share the same potenital difference."),
        ("c", "Elements in parallel share the same current."),
        ("d", "Elements in parallel share the same potential difference."),
        ("e", "Any elements ties together at one node are in series."),
        ("f", "Any elements ties together at two nodes are in parallel."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS,required=False)

class DLR8_2Form(forms.Form):
    OPTIONS = (
        ("a", "The effective resistance of the parallel combination increases as R\N{SUBSCRIPT TWO} decreases."),
        ("b", 'The effective resistance of the parallel combination decreases as R\N{SUBSCRIPT TWO} decreases.'),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS,required=False)

class DLR8_3Form(forms.Form):
    OPTIONS = (
        ("a", "Since the voltage source is ideal, the current associated with the voltage source will not change as the value of R\N{SUBSCRIPT TWO} changes."),
        ("b", "Since the voltage source is ideal, the power associated with the voltage source will not change as the value of R\N{SUBSCRIPT TWO} changes."),
        ("c", "Since the voltage source is ideal, the potential difference across the voltage source will not change as the calue of R\N{SUBSCRIPT TWO} changes."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS,required=False)

class DLR8_4Form(forms.Form):
    OPTIONS = (
        ("a", "Since the value of R\N{SUBSCRIPT ONE}'s resistance is constant while its current increases, resistor R\N{SUBSCRIPT ONE} must dissipate MORE power as the resistance of R\N{SUBSCRIPT TWO} decreases."),
        ("b", "Since the value of R\N{SUBSCRIPT ONE}'s resistance is constant while its current increases, resistor R\N{SUBSCRIPT ONE} must dissipate LESS power as the resistance of R\N{SUBSCRIPT TWO} decreases."),
        ("c", "The increase in current in resistor R\N{SUBSCRIPT ONE} causes more potential difference across R\N{SUBSCRIPT ONE}."),
        ("d", "The increase in current in resistor R\N{SUBSCRIPT ONE} is caused by an increase in potential difference across R\N{SUBSCRIPT ONE}."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS,required=False)

class DLR8_5Form(forms.Form):
    OPTIONS = (
        ("a", "The current in the equivalent resistance R\N{SUBSCRIPT TWO}\N{SUBSCRIPT THREE} is the same as that through R\N{SUBSCRIPT ONE}."),
        ("b", "The current in the equivalent resistance R\N{SUBSCRIPT TWO}\N{SUBSCRIPT THREE} is less than the current in R\N{SUBSCRIPT ONE}."),
        ("c", "The potential difference across the parallel resistance R\N{SUBSCRIPT TWO}\N{SUBSCRIPT THREE}, V_R\N{SUBSCRIPT TWO}\N{SUBSCRIPT THREE}, decreases as R\N{SUBSCRIPT TWO} decreases."),
        ("d", "The potential difference across the parallel resistance R\N{SUBSCRIPT TWO}\N{SUBSCRIPT THREE}, V_R\N{SUBSCRIPT TWO}\N{SUBSCRIPT THREE}, increases as R\N{SUBSCRIPT TWO} decreases."),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS,required=False)

class DLR8_6Form(forms.Form):
    OPTIONS = (
        ("a", "P_V\N{Latin Subscript Small Letter S}=V\N{Latin Subscript Small Letter S}\N{SUPERSCRIPT TWO}/R\N{SUBSCRIPT ONE}"),
        ("b", "P_V\N{Latin Subscript Small Letter S}=V\N{Latin Subscript Small Letter S}\N{SUPERSCRIPT TWO}/(R\N{SUBSCRIPT ONE}+R\N{SUBSCRIPT THREE})"),
        ("c", "I\N{Latin Subscript Small Letter S}=V\N{Latin Subscript Small Letter S}/(R\N{SUBSCRIPT ONE}+R\N{SUBSCRIPT THREE})"),
        ("d", "P_R\N{SUBSCRIPT THREE}=0"),
        ("e", "P_R\N{SUBSCRIPT TWO}=0"),
        ("f", "I_R\N{SUBSCRIPT ONE}=I_R\N{SUBSCRIPT TWO}"),
    )
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS,required=False)

class DLR8_7Form(forms.ModelForm):

    correctPath_confidence = forms.CharField(widget=forms.Select(choices=CONFIDENCE_CHOICES), required=True)   

    class Meta:
        model = StudentsDb
        fields = ('correctPath_feedback_on_feedback',)

    def __init__(self, *args, **kwargs):
        super(DLR8_7Form, self).__init__(*args, **kwargs)
        # self.fields['post_confidence'].required = True
        self.fields['correctPath_feedback_on_feedback'].required = True