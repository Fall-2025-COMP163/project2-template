import pytest
from project2_starter import Character, Warrior, Mage, Rogue, Weapon

class TestWarriorSpecialAbilities:
    """Test warrior-specific special abilities"""
    
    def test_warrior_has_power_strike(self):
        """Test that warriors have power_strike ability"""
        warrior = Warrior("PowerWarrior")
        
        assert hasattr(warrior, 'power_strike'), "Warrior should have power_strike ability"
        assert callable(getattr(warrior, 'power_strike')), "power_strike should be callable"

    def test_power_strike_works(self):
        """Test that power_strike ability functions correctly"""
        warrior = Warrior("StrikeWarrior")
        target = Character("StrikeTarget", 100, 0, 0)
        
        original_health = target.health
        warrior.power_strike(target)
        
        assert target.health < original_health, "Power strike should damage target"
        damage_dealt = original_health - target.health
        assert damage_dealt > 0, "Power strike should deal damage"

    def test_power_strike_does_more_damage_than_normal_attack(self):
        """Test that power_strike does more damage than regular attack"""
        warrior = Warrior("CompareWarrior")
        
        # Test normal attack
        target1 = Character("NormalTarget", 100, 0, 0)
        warrior.attack(target1)
        normal_damage = 100 - target1.health
        
        # Test power strike
        target2 = Character("PowerTarget", 100, 0, 0)
        warrior.power_strike(target2)
        power_damage = 100 - target2.health
        
        assert power_damage > normal_damage, "Power strike should do more damage than normal attack"

class TestMageSpecialAbilities:
    """Test mage-specific special abilities"""
    
    def test_mage_has_fireball(self):
        """Test that mages have fireball ability"""
        mage = Mage("FireMage")
        
        assert hasattr(mage, 'fireball'), "Mage should have fireball ability"
        assert callable(getattr(mage, 'fireball')), "fireball should be callable"

    def test_fireball_works(self):
        """Test that fireball ability functions correctly"""
        mage = Mage("BallMage")
        target = Character("FireTarget", 100, 0, 0)
        
        original_health = target.health
        mage.fireball(target)
        
        assert target.health < original_health, "Fireball should damage target"
        damage_dealt = original_health - target.health
        assert damage_dealt > 0, "Fireball should deal damage"

    def test_fireball_does_significant_damage(self):
        """Test that fireball does meaningful damage"""
        mage = Mage("MagicMage")
        target = Character("MagicTarget", 100, 0, 0)
        
        mage.fireball(target)
        damage_dealt = 100 - target.health
        
        # Fireball should do reasonable damage (at least 10, not more than 50)
        assert 10 <= damage_dealt <= 50, "Fireball should do significant but reasonable damage"

class TestRogueSpecialAbilities:
    """Test rogue-specific special abilities"""
    
    def test_rogue_has_sneak_attack(self):
        """Test that rogues have sneak_attack ability"""
        rogue = Rogue("SneakRogue")
        
        assert hasattr(rogue, 'sneak_attack'), "Rogue should have sneak_attack ability"
        assert callable(getattr(rogue, 'sneak_attack')), "sneak_attack should be callable"

    def test_sneak_attack_works(self):
        """Test that sneak_attack ability functions correctly"""
        rogue = Rogue("AttackRogue")
        target = Character("SneakTarget", 100, 0, 0)
        
        original_health = target.health
        rogue.sneak_attack(target)
        
        assert target.health < original_health, "Sneak attack should damage target"
        damage_dealt = original_health - target.health
        assert damage_dealt > 0, "Sneak attack should deal damage"

    def test_sneak_attack_does_high_damage(self):
        """Test that sneak_attack does high damage (critical hit)"""
        rogue = Rogue("CritRogue")
        target = Character("CritTarget", 100, 0, 0)
        
        rogue.sneak_attack(target)
        damage_dealt = 100 - target.health
        
        # Sneak attack should do high damage
        assert damage_dealt >= 15, "Sneak attack should do high damage"

class TestSpecialAbilityComparison:
    """Test that special abilities work differently from normal attacks"""
    
    def test_special_abilities_vs_normal_attacks(self):
        """Test that special abilities generally do more damage than normal attacks"""
        warrior = Warrior("SpecialWarrior")
        mage = Mage("SpecialMage")
        rogue = Rogue("SpecialRogue")
        
        # Test normal attacks
        normal_targets = [Character("Normal1", 100, 0, 0), Character("Normal2", 100, 0, 0), Character("Normal3", 100, 0, 0)]
        warrior.attack(normal_targets[0])
        mage.attack(normal_targets[1])
        rogue.attack(normal_targets[2])
        
        normal_damages = [100 - target.health for target in normal_targets]
        
        # Test special abilities
        special_targets = [Character("Special1", 100, 0, 0), Character("Special2", 100, 0, 0), Character("Special3", 100, 0, 0)]
        warrior.power_strike(special_targets[0])
        mage.fireball(special_targets[1])
        rogue.sneak_attack(special_targets[2])
        
        special_damages = [100 - target.health for target in special_targets]
        
        # Special abilities should generally do more damage
        assert special_damages[0] >= normal_damages[0], "Warrior power strike should do at least as much as normal attack"
        assert special_damages[1] >= normal_damages[1], "Mage fireball should do at least as much as normal attack"
        assert special_damages[2] >= normal_damages[2], "Rogue sneak attack should do at least as much as normal attack"

    def test_all_special_abilities_are_unique(self):
        """Test that each character has different special abilities"""
        warrior = Warrior("UniqueWarrior")
        mage = Mage("UniqueMage")
        rogue = Rogue("UniqueRogue")
        
        # Each should have their own unique ability
        assert hasattr(warrior, 'power_strike'), "Warrior should have power_strike"
        assert hasattr(mage, 'fireball'), "Mage should have fireball"
        assert hasattr(rogue, 'sneak_attack'), "Rogue should have sneak_attack"
        
        # Others should not have these abilities
        assert not hasattr(mage, 'power_strike'), "Mage should not have warrior ability"
        assert not hasattr(rogue, 'fireball'), "Rogue should not have mage ability"
        assert not hasattr(warrior, 'sneak_attack'), "Warrior should not have rogue ability"

class TestWeaponComposition:
    """Test weapon composition functionality"""
    
    def test_weapon_creation(self):
        """Test that weapons can be created with proper attributes"""
        sword = Weapon("Iron Sword", 10)
        
        assert hasattr(sword, 'name'), "Weapon should have name attribute"
        assert hasattr(sword, 'damage_bonus'), "Weapon should have damage_bonus attribute"
        
        assert sword.name == "Iron Sword", "Weapon name should be set correctly"
        assert sword.damage_bonus == 10, "Weapon damage bonus should be set correctly"

    def test_weapon_display_info(self):
        """Test that weapons can display their information"""
        staff = Weapon("Magic Staff", 15)
        
        assert hasattr(staff, 'display_info'), "Weapon should have display_info method"
        assert callable(getattr(staff, 'display_info')), "display_info should be callable"
        
        # Method should run without error
        result = staff.display_info()
        assert result is None, "display_info should return None (just prints)"

    def test_multiple_weapon_types(self):
        """Test creating different weapon types"""
        weapons = [
            Weapon("Iron Sword", 10),
            Weapon("Magic Staff", 15),
            Weapon("Steel Dagger", 8),
            Weapon("War Hammer", 20)
        ]
        
        for weapon in weapons:
            assert hasattr(weapon, 'name'), f"Weapon {weapon.name} should have name"
            assert hasattr(weapon, 'damage_bonus'), f"Weapon {weapon.name} should have damage_bonus"
            assert isinstance(weapon.damage_bonus, (int, float)), f"Damage bonus should be a number"
            assert weapon.damage_bonus > 0, f"Damage bonus should be positive"

    def test_weapon_damage_bonus_types(self):
        """Test that weapons accept different damage bonus values"""
        low_damage = Weapon("Rusty Knife", 5)
        medium_damage = Weapon("Iron Sword", 15)
        high_damage = Weapon("Dragon Slayer", 25)
        
        assert low_damage.damage_bonus == 5, "Low damage weapon should work"
        assert medium_damage.damage_bonus == 15, "Medium damage weapon should work"
        assert high_damage.damage_bonus == 25, "High damage weapon should work"

class TestCompositionVsInheritance:
    """Test understanding of composition vs inheritance"""
    
    def test_weapon_is_not_character(self):
        """Test that Weapon is separate from Character hierarchy (composition, not inheritance)"""
        sword = Weapon("Test Sword", 12)
        warrior = Warrior("Test Warrior")
        
        # Weapon should NOT be a Character
        assert not isinstance(sword, Character), "Weapon should not inherit from Character"
        
        # But Warrior should be a Character
        assert isinstance(warrior, Character), "Warrior should inherit from Character"

    def test_characters_can_have_weapons(self):
        """Test that characters can be associated with weapons (composition)"""
        warrior = Warrior("ArmedWarrior")
        sword = Weapon("Warrior Sword", 15)
        
        # This is composition - character HAS a weapon
        # We're not testing specific implementation, just that it's possible
        # Students might implement this in different ways
        
        # Both objects should exist independently
        assert warrior is not None, "Character should exist"
        assert sword is not None, "Weapon should exist"
        
        # They should be different types
        assert type(warrior) != type(sword), "Character and Weapon should be different types"

class TestDamageCalculations:
    """Test that damage calculations work reasonably"""
    
    def test_damage_is_consistent(self):
        """Test that repeated attacks do consistent damage"""
        warrior = Warrior("ConsistentWarrior")
        
        damages = []
        for i in range(3):
            target = Character("Target", 100, 0, 0)
            warrior.attack(target)
            damage = 100 - target.health
            damages.append(damage)
        
        # All damages should be reasonable
        for damage in damages:
            assert 5 <= damage <= 50, "Damage should be in reasonable range"

    def test_special_abilities_do_reasonable_damage(self):
        """Test that all special abilities do reasonable amounts of damage"""
        warrior = Warrior("ReasonableWarrior")
        mage = Mage("ReasonableMage")
        rogue = Rogue("ReasonableRogue")
        
        targets = [Character("Target1", 100, 0, 0), Character("Target2", 100, 0, 0), Character("Target3", 100, 0, 0)]
        
        warrior.power_strike(targets[0])
        mage.fireball(targets[1])
        rogue.sneak_attack(targets[2])
        
        damages = [100 - target.health for target in targets]
        
        # All special abilities should do reasonable damage
        for i, damage in enumerate(damages):
            assert 10 <= damage <= 50, f"Special ability {i} should do reasonable damage"

class TestErrorHandling:
    """Test basic error handling and edge cases"""
    
    def test_zero_damage_handling(self):
        """Test that characters can handle zero or minimal damage"""
        char = Character("EdgeChar", 100, 10, 5)
        
        original_health = char.health
        char.take_damage(0)
        
        assert char.health == original_health, "Zero damage should not change health"

    def test_excessive_damage_handling(self):
        """Test that characters handle damage greater than their health"""
        char = Character("OverChar", 50, 10, 5)
        
        char.take_damage(100)  # More than max health
        
        assert char.health >= 0, "Health should not go below 0"
        assert char.health <= 0, "Character should be defeated"
