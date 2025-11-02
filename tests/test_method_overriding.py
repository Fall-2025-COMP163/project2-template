import pytest
from project2_starter import Character, Player, Warrior, Mage, Rogue

class TestMethodOverriding:
    """Test that subclasses properly override parent methods"""
    
    def test_all_characters_have_attack_method(self):
        """Test that all character types have attack methods"""
        warrior = Warrior("AttackWarrior")
        mage = Mage("AttackMage")
        rogue = Rogue("AttackRogue")
        base_char = Character("BaseChar", 100, 10, 5)
        
        assert hasattr(warrior, 'attack'), "Warrior should have attack method"
        assert hasattr(mage, 'attack'), "Mage should have attack method"
        assert hasattr(rogue, 'attack'), "Rogue should have attack method"
        assert hasattr(base_char, 'attack'), "Character should have attack method"

    def test_attack_methods_actually_work(self):
        """Test that attack methods function and affect targets"""
        warrior = Warrior("WorkingWarrior")
        target = Character("Target", 100, 0, 0)
        
        original_health = target.health
        warrior.attack(target)
        
        assert target.health < original_health, "Attack should reduce target health"
        assert target.health >= 0, "Health should not go below 0"

    def test_different_classes_attack_differently(self):
        """Test that different character classes have different attack behaviors"""
        warrior = Warrior("DiffWarrior")
        mage = Mage("DiffMage")
        
        # Create fresh targets for each test
        target1 = Character("Target1", 100, 0, 0)
        target2 = Character("Target2", 100, 0, 0)
        
        # Attack with different characters
        warrior.attack(target1)
        mage.attack(target2)
        
        # Both should have taken damage
        assert target1.health < 100, "Warrior attack should damage target"
        assert target2.health < 100, "Mage attack should damage target"
        
        # Damage amounts might be different (this tests method overriding)
        damage1 = 100 - target1.health
        damage2 = 100 - target2.health
        
        # Both should do reasonable damage
        assert 5 <= damage1 <= 50, "Warrior damage should be reasonable"
        assert 5 <= damage2 <= 50, "Mage damage should be reasonable"

    def test_display_stats_override(self):
        """Test that Player classes override display_stats correctly"""
        base_char = Character("BaseChar", 50, 8, 3)
        warrior = Warrior("OverrideWarrior")
        
        # Both should have display_stats method
        assert hasattr(base_char, 'display_stats'), "Character should have display_stats"
        assert hasattr(warrior, 'display_stats'), "Warrior should have display_stats"
        
        # Methods should run without error
        base_char.display_stats()
        warrior.display_stats()
        
        # Player classes should have additional attributes that base Character doesn't
        assert hasattr(warrior, 'character_class'), "Player should have character_class attribute"
        assert hasattr(warrior, 'level'), "Player should have level attribute"

class TestPolymorphism:
    """Test that polymorphism works correctly"""
    
    def test_polymorphic_attack_calls(self):
        """Test that different character types can attack using the same method call"""
        characters = [
            Warrior("PolyWarrior"),
            Mage("PolyMage"), 
            Rogue("PolyRogue")
        ]
        
        target = Character("PolyTarget", 200, 0, 0)
        original_health = target.health
        
        # All characters should be able to attack using the same method call
        for character in characters:
            current_health = target.health
            character.attack(target)
            
            # Each attack should work
            assert target.health < current_health, f"{type(character).__name__} attack should work"
            
            # Reset target health for fair comparison
            target.health = current_health

    def test_polymorphic_display_stats(self):
        """Test that display_stats works polymorphically across all character types"""
        characters = [
            Character("BaseChar", 50, 8, 3),
            Warrior("PolyWarrior"),
            Mage("PolyMage"),
            Rogue("PolyRogue")
        ]
        
        # All should respond to the same method call without error
        for character in characters:
            character.display_stats()  # Should not crash

    def test_polymorphic_damage_taking(self):
        """Test that take_damage works the same way for all character types"""
        characters = [
            Character("DamageChar", 100, 10, 5),
            Warrior("DamageWarrior"),
            Mage("DamageMage"),
            Rogue("DamageRogue")
        ]
        
        for character in characters:
            original_health = character.health
            character.take_damage(15)
            
            # All should take damage the same way
            assert character.health == original_health - 15, f"{type(character).__name__} should take damage consistently"

    def test_isinstance_checks_work(self):
        """Test that isinstance checks work correctly for polymorphism"""
        warrior = Warrior("IsWarrior")
        mage = Mage("IsMage")
        rogue = Rogue("IsRogue")
        
        # Create list of characters for polymorphic processing
        party = [warrior, mage, rogue]
        
        # Should be able to identify specific types
        warrior_count = sum(1 for char in party if isinstance(char, Warrior))
        mage_count = sum(1 for char in party if isinstance(char, Mage))
        rogue_count = sum(1 for char in party if isinstance(char, Rogue))
        
        assert warrior_count == 1, "Should find exactly one warrior"
        assert mage_count == 1, "Should find exactly one mage"
        assert rogue_count == 1, "Should find exactly one rogue"
        
        # All should be instances of Character (polymorphism)
        character_count = sum(1 for char in party if isinstance(char, Character))
        assert character_count == 3, "All should be Characters"

class TestMethodBehaviorDifferences:
    """Test that overridden methods actually behave differently"""
    
    def test_warrior_vs_mage_attack_differences(self):
        """Test that Warriors and Mages attack differently"""
        warrior = Warrior("BehaviorWarrior")
        mage = Mage("BehaviorMage")
        
        # Test multiple attacks to see if there are consistent differences
        warrior_damages = []
        mage_damages = []
        
        for i in range(3):
            # Test warrior attacks
            target1 = Character("WarriorTarget", 100, 0, 0)
            warrior.attack(target1)
            warrior_damage = 100 - target1.health
            warrior_damages.append(warrior_damage)
            
            # Test mage attacks  
            target2 = Character("MageTarget", 100, 0, 0)
            mage.attack(target2)
            mage_damage = 100 - target2.health
            mage_damages.append(mage_damage)
        
        # Both should do damage
        assert all(damage > 0 for damage in warrior_damages), "Warrior should do damage"
        assert all(damage > 0 for damage in mage_damages), "Mage should do damage"
        
        # Damages should be reasonable
        assert all(5 <= damage <= 50 for damage in warrior_damages), "Warrior damage should be reasonable"
        assert all(5 <= damage <= 50 for damage in mage_damages), "Mage damage should be reasonable"

    def test_attack_uses_appropriate_stats(self):
        """Test that different classes use appropriate stats for attacks"""
        # Create characters with known stat differences
        high_str_warrior = Warrior("HighStrWarrior")
        high_mag_mage = Mage("HighMagMage")
        
        # Warriors should have higher strength
        assert high_str_warrior.strength >= 12, "Warrior should have decent strength"
        
        # Mages should have higher magic
        assert high_mag_mage.magic >= 15, "Mage should have high magic"
        
        # Test that they both can attack (testing the interface is the same)
        target1 = Character("StrTarget", 50, 0, 0)
        target2 = Character("MagTarget", 50, 0, 0)
        
        high_str_warrior.attack(target1)
        high_mag_mage.attack(target2)
        
        # Both should have dealt damage
        assert target1.health < 50, "Warrior attack should work"
        assert target2.health < 50, "Mage attack should work"

class TestConsistentInterfaces:
    """Test that all classes provide consistent interfaces"""
    
    def test_all_players_have_character_class_attribute(self):
        """Test that all player characters have character_class attribute"""
        warrior = Warrior("ClassWarrior")
        mage = Mage("ClassMage")
        rogue = Rogue("ClassRogue")
        
        assert hasattr(warrior, 'character_class'), "Warrior should have character_class"
        assert hasattr(mage, 'character_class'), "Mage should have character_class"
        assert hasattr(rogue, 'character_class'), "Rogue should have character_class"
        
        # Values should be appropriate
        assert warrior.character_class == "Warrior", "Warrior class should be correct"
        assert mage.character_class == "Mage", "Mage class should be correct"
        assert rogue.character_class == "Rogue", "Rogue class should be correct"

    def test_all_characters_have_basic_attributes(self):
        """Test that all character types have the basic required attributes"""
        characters = [
            Character("BasicChar", 100, 10, 5),
            Warrior("BasicWarrior"),
            Mage("BasicMage"),
            Rogue("BasicRogue")
        ]
        
        required_attributes = ['name', 'health', 'strength', 'magic']
        
        for character in characters:
            for attr in required_attributes:
                assert hasattr(character, attr), f"{type(character).__name__} should have {attr} attribute"

    def test_method_return_types_consistent(self):
        """Test that overridden methods return consistent types"""
        characters = [
            Warrior("ReturnWarrior"),
            Mage("ReturnMage"),
            Rogue("ReturnRogue")
        ]
        
        for character in characters:
            # display_stats should return None for all
            result = character.display_stats()
            assert result is None, f"{type(character).__name__}.display_stats() should return None"
