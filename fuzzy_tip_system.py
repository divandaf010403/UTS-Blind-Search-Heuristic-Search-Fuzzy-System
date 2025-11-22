"""
Fuzzy Logic System for Restaurant Tip Calculation
Nama: Divanda Firdaus
NIM: 32602500023

Based on the problem:
- Food Quality (0-10): Bad (0,0,5), Good (5,10,10)
- Service Quality (0-10): Poor (0,0,5), Excellent (5,10,10)
- Tip Percentage (0-20): Low (0,0,10), High (10,20,20)

Rules:
1. IF Service is Poor OR Food is Bad THEN Tip is Low
2. IF Service is Excellent AND Food is Good THEN Tip is High
"""

class FuzzySet:
    def __init__(self, name, a, b, c):
        """
        Triangular membership function
        name: string name of the fuzzy set
        a, b, c: parameters for triangular function (a, b, c)
        """
        self.name = name
        self.a = a
        self.b = b
        self.c = c
    
    def membership(self, x):
        """Calculate membership value for x using triangular function"""
        if x <= self.a or x >= self.c:
            return 0.0
        elif x == self.b:
            return 1.0
        elif self.a < x < self.b:
            return (x - self.a) / (self.b - self.a)
        else:  # self.b < x < self.c
            return (self.c - x) / (self.c - self.b)
    
    def __str__(self):
        return f"{self.name}: ({self.a}, {self.b}, {self.c})"


class FuzzyVariable:
    def __init__(self, name, min_val, max_val):
        self.name = name
        self.min_val = min_val
        self.max_val = max_val
        self.sets = {}
    
    def add_set(self, set_name, a, b, c):
        """Add a fuzzy set to this variable"""
        self.sets[set_name] = FuzzySet(set_name, a, b, c)
    
    def fuzzify(self, value):
        """Convert crisp value to fuzzy memberships"""
        memberships = {}
        for set_name, fuzzy_set in self.sets.items():
            memberships[set_name] = fuzzy_set.membership(value)
        return memberships


class FuzzyRule:
    def __init__(self, antecedents, consequent, operator='AND'):
        """
        antecedents: list of (variable_name, set_name) tuples
        consequent: (variable_name, set_name) tuple
        operator: 'AND' or 'OR' for combining antecedents
        """
        self.antecedents = antecedents
        self.consequent = consequent
        self.operator = operator
    
    def evaluate(self, input_memberships):
        """Evaluate rule strength based on input memberships"""
        strengths = []
        
        for var_name, set_name in self.antecedents:
            if var_name in input_memberships and set_name in input_memberships[var_name]:
                strengths.append(input_memberships[var_name][set_name])
            else:
                strengths.append(0.0)
        
        if self.operator == 'AND':
            return min(strengths)
        elif self.operator == 'OR':
            return max(strengths)
        else:
            return 0.0


class FuzzySystem:
    def __init__(self):
        self.variables = {}
        self.rules = []
        self.setup_tip_system()
    
    def setup_tip_system(self):
        """Setup the restaurant tip fuzzy system"""
        # Input variables
        food_quality = FuzzyVariable("Food Quality", 0, 10)
        food_quality.add_set("Bad", 0, 0, 5)
        food_quality.add_set("Good", 5, 10, 10)
        self.variables["Food Quality"] = food_quality
        
        service_quality = FuzzyVariable("Service Quality", 0, 10)
        service_quality.add_set("Poor", 0, 0, 5)
        service_quality.add_set("Excellent", 5, 10, 10)
        self.variables["Service Quality"] = service_quality
        
        # Output variable
        tip = FuzzyVariable("Tip", 0, 20)
        tip.add_set("Low", 0, 0, 10)
        tip.add_set("High", 10, 20, 20)
        self.variables["Tip"] = tip
        
        # Fuzzy rules
        rule1 = FuzzyRule(
            antecedents=[("Service Quality", "Poor"), ("Food Quality", "Bad")],
            consequent=("Tip", "Low"),
            operator="OR"
        )
        
        rule2 = FuzzyRule(
            antecedents=[("Service Quality", "Excellent"), ("Food Quality", "Good")],
            consequent=("Tip", "High"),
            operator="AND"
        )
        
        self.rules = [rule1, rule2]
    
    def fuzzify_inputs(self, food_quality, service_quality):
        """Convert crisp inputs to fuzzy memberships"""
        input_memberships = {}
        
        input_memberships["Food Quality"] = self.variables["Food Quality"].fuzzify(food_quality)
        input_memberships["Service Quality"] = self.variables["Service Quality"].fuzzify(service_quality)
        
        return input_memberships
    
    def apply_rules(self, input_memberships):
        """Apply fuzzy rules to get output memberships"""
        output_memberships = {"Low": 0.0, "High": 0.0}
        
        for rule in self.rules:
            rule_strength = rule.evaluate(input_memberships)
            output_set = rule.consequent[1]
            output_memberships[output_set] = max(output_memberships[output_set], rule_strength)
        
        return output_memberships
    
    def defuzzify(self, output_memberships):
        """Convert fuzzy output to crisp value using centroid method"""
        tip_var = self.variables["Tip"]
        
        # Sample points for centroid calculation
        samples = 100
        step = (tip_var.max_val - tip_var.min_val) / samples
        numerator = 0.0
        denominator = 0.0
        
        for i in range(samples + 1):
            x = tip_var.min_val + i * step
            
            # Find maximum membership at this point
            max_membership = 0.0
            for set_name, membership_strength in output_memberships.items():
                if membership_strength > 0:
                    set_membership = tip_var.sets[set_name].membership(x)
                    combined_membership = min(set_membership, membership_strength)
                    max_membership = max(max_membership, combined_membership)
            
            numerator += x * max_membership
            denominator += max_membership
        
        if denominator == 0:
            return 0.0
        
        return numerator / denominator
    
    def calculate_tip(self, food_quality, service_quality):
        """Main method to calculate tip percentage"""
        print(f"Calculating tip for Food Quality: {food_quality}, Service Quality: {service_quality}")
        print("=" * 60)
        
        # Step 1: Fuzzification
        print("Step 1: Fuzzification")
        input_memberships = self.fuzzify_inputs(food_quality, service_quality)
        
        for var_name, memberships in input_memberships.items():
            print(f"{var_name}:")
            for set_name, membership in memberships.items():
                print(f"  {set_name}: {membership:.3f}")
        
        # Step 2: Rule Evaluation
        print("\nStep 2: Rule Evaluation")
        output_memberships = self.apply_rules(input_memberships)
        
        for i, rule in enumerate(self.rules, 1):
            rule_strength = rule.evaluate(input_memberships)
            print(f"Rule {i}: {rule_strength:.3f}")
        
        print(f"\nOutput memberships:")
        for set_name, membership in output_memberships.items():
            print(f"  {set_name}: {membership:.3f}")
        
        # Step 3: Defuzzification
        print("\nStep 3: Defuzzification")
        tip_percentage = self.defuzzify(output_memberships)
        print(f"Final tip percentage: {tip_percentage:.2f}%")
        
        return tip_percentage


# Test the system
if __name__ == "__main__":
    # Create fuzzy system
    fuzzy_system = FuzzySystem()
    
    # Test case from the problem
    food_quality = 7
    service_quality = 3
    
    print("Restaurant Tip Calculation Using Fuzzy Logic")
    print("=" * 60)
    
    tip_percentage = fuzzy_system.calculate_tip(food_quality, service_quality)
    
    print("\n" + "=" * 60)
    print(f"RESULT: For Food Quality = {food_quality} and Service Quality = {service_quality}")
    print(f"Recommended Tip: {tip_percentage:.2f}%")
    
    # Additional test cases
    print("\n" + "=" * 60)
    print("Additional Test Cases:")
    
    test_cases = [
        (2, 2),   # Low food, low service
        (8, 8),   # High food, high service
        (5, 5),   # Medium values
        (9, 1),   # High food, low service
        (1, 9),   # Low food, high service
    ]
    
    for food, service in test_cases:
        tip = fuzzy_system.calculate_tip(food, service)
        print(f"\nFood Quality: {food}, Service Quality: {service} -> Tip: {tip:.2f}%")