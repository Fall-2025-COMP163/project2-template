import pytest
from project2_starter import Character, Player, Warrior, Mage, Rogue, Weapon

class TestClassCreation:
    """Test that all required classes can be created"""
    
    def test_all_classes_exist(self):
        """Test that all required classes can be imported and instantiated"""
        # This test passes if all imports work without error
        assert Character is not None, "Character class should exist"
        assert Player is not None, "Player class should exist"
        assert Warrior is not None, "Warrior class should exist"
        assert Mage is not None, "Mage class should exist"
        assert Rogue is not None, "Rogue class should exist"
        assert Weapon is not None, "Weapon class should exist"

    def test_character_base_class_creation(self):
        """Test base Character class can be created with proper attributes"""
        char = Character("BaseChar", 100, 10, 5)
        
        assert hasattr(char, 'name'), "Character should have name attribute"
        assert hasattr(char, 'health'), "Character should have health attribute"
        assert hasattr(char, 'strength'), "Character should have strength attribute"
        assert hasattr(char, 'magic'), "Character should have magic attribute"
        
        assert char.name == "BaseChar", "Name should be set correctly"
        assert char.health == 100, "Health should be set correctly"
        assert char.strength == 10, "Strength should be set correctly"
        assert char.magic == 5, "Magic should be set correctly"

    def test_warrior_creation(self):
        """Test Warrior character creation and stats"""
        warrior = Warrior("TestWarrior")
        
        assert hasattr(warrior, 'name'), "Warrior should have name"
        assert hasattr(warrior, 'health'), "Warrior should have health"
        assert hasattr(warrior, 'strength'), "Warrior should have strength"
        assert hasattr(warrior, 'magic'), "Warrior should have magic"
        assert hasattr(warrior, 'character_class'), "Warrior should have character_class"
        
        assert warrior.name == "TestWarrior", "Warrior name should be set correctly"
        assert isinstance(warrior.health, (int, float)), "Health should be a number"
        assert isinstance(warrior.strength, (int, float)), "Strength should be a number"
        assert isinstance(warrior.magic, (int, float)), "Magic should be a number"
        
        # Warriors should be strong and tough
        assert warrior.health >= 100, "Warriors should have high health"
        assert warrior.strength >= 12, "Warriors should have decent strength"

    def test_mage_creation(self):
        """Test Mage character creation and stats"""
        mage = Mage("TestMage")
        
        assert hasattr(mage, 'name'), "Mage should have name"
        assert hasattr(mage, 'health'), "Mage should have health"
        assert hasattr(mage, 'magic'), "Mage should have magic attribute"
        assert hasattr(mage, 'character_class'), "Mage should have character_class"
        
        assert mage.name == "TestMage", "Mage name should be set correctly"
        assert mage.magic >= 15, "Mages should have high magic"
        assert mage.health >= 50, "Mages should have reasonable health"

    def test_rogue_creation(self):
        """Test Rogue character creation and stats"""
        rogue = Rogue("TestRogue")
        
        assert hasattr(rogue, 'name'), "Rogue should have name"
        assert hasattr(rogue, 'health'), "Rogue should have health"
        assert hasattr(rogue, 'strength'), "Rogue should have strength"
        assert hasattr(rogue, 'magic'), "Rogue should have magic"
        assert hasattr(rogue, 'character_class'), "Rogue should have character_class"
        
        assert rogue.name == "TestRogue", "Rogue name should be set correctly"
        assert rogue.health >= 70, "Rogues should have decent health"

class TestInheritanceHierarchy:
    """Test that the 3-level inheritance chain works correctly"""
    
    def test_warrior_inheritance_chain(self):
        """Test that Warrior inherits properly through the chain"""
        warrior = Warrior("InheritanceWarrior")
        
        # Test 3-level inheritance: Warrior → Player → Character
        assert isinstance(warrior, Warrior), "Should be instance of Warrior"
        assert isinstance(warrior, Player), "Should be instance of Player (inheritance)"
        assert isinstance(warrior, Character), "Should be instance of Character (inheritance)"

    def test_mage_inheritance_chain(self):
        """Test that Mage inherits properly through the chain"""
        mage = Mage("InheritanceMage")
        
        assert isinstance(mage, Mage), "Should be instance of Mage"
        assert isinstance(mage, Player), "Should be instance of Player (inheritance)"
        assert isinstance(mage, Character), "Should be instance of Character (inheritance)"

    def test_rogue_inheritance_chain(self):
        """Test that Rogue inherits properly through the chain"""
        rogue = Rogue("InheritanceRogue")
        
        assert isinstance(rogue, Rogue), "Should be instance of Rogue"
        assert isinstance(rogue, Player), "Should be instance of Player (inheritance)"
        assert isinstance(rogue, Character), "Should be instance of Character (inheritance)"

    def test_player_inheritance_from_character(self):
        """Test that Player inherits from Character"""
        # Test by creating a Player directly (if possible)
        # This tests the middle layer of inheritance
        if hasattr(Player, '__init__'):
            player = Player("TestPlayer", "TestClass", 100, 10, 10)
            assert isinstance(player, Player), "Should be instance of Player"
            assert isinstance(player, Character), "Should be instance of Character (inheritance)"

class TestRequiredMethods:
    """Test that all classes have required methods"""
    
    def test_character_has_required_methods(self):
        """Test that Character class has all required methods"""
        char = Character("MethodChar", 50, 8, 3)
        
        assert hasattr(char, 'attack'), "Character should have attack method"
        assert hasattr(char, 'take_damage'), "Character should have take_damage method"
        assert hasattr(char, 'display_stats'), "Character should have display_stats method"

    def test_player_has_required_methods(self):
        """Test that Player classes have all required methods"""
        warrior = Warrior("MethodWarrior")
        
        # Should have all Character methods
        assert hasattr(warrior, 'attack'), "Player should have attack method"
        assert hasattr(warrior, 'take_damage'), "Player should have take_damage method"
        assert hasattr(warrior, 'display_stats'), "Player should have display_stats method"

    def test_all_players_have_display_stats(self):
        """Test that all player types have display_stats method"""
        characters = [
            Warrior("DisplayWarrior"),
            Mage("DisplayMage"),
            Rogue("DisplayRogue")
        ]
        
        for character in characters:
            assert hasattr(character, 'display_stats'), f"{type(character).__name__} should have display_stats method"
            # Method should run without error
            character.display_stats()

class TestBasicMechanics:
    """Test basic game mechanics work"""
    
    def test_take_damage_reduces_health(self):
        """Test that take_damage reduces character health"""
        char = Character("DamageChar", 100, 10, 5)
        
        original_health = char.health
        char.take_damage(20)
        
        assert char.health == original_health - 20, "Health should be reduced by damage amount"

    def test_health_cannot_go_negative(self):
        """Test that health stops at 0"""
        char = Character("ZeroChar", 50, 10, 5)
        
        char.take_damage(100)  # More damage than health
        
        assert char.health >= 0, "Health should not go below 0"

    def test_super_calls_work(self):
        """Test that super() calls work in inheritance"""
        warrior = Warrior("SuperTest")
        
        # Player should call Character.__init__
        # Warrior should call Player.__init__
        # All attributes should be set correctly
        assert hasattr(warrior, 'name'), "Super calls should set name"
        assert hasattr(warrior, 'health'), "Super calls should set health"
        assert hasattr(warrior, 'character_class'), "Super calls should set character_class"

class TestStatDistributions:
    """Test that different classes have appropriate stat distributions"""
    
    def test_classes_have_different_stats(self):
        """Test that warrior, mage, rogue have different stat distributions"""
        warrior = Warrior("StatWarrior")
        mage = Mage("StatMage")
        rogue = Rogue("StatRogue")
        
        # At least one stat should be different between classes
        warrior_mage_different = (
            warrior.health != mage.health or
            warrior.strength != mage.strength or
            warrior.magic != mage.magic
        )
        assert warrior_mage_different, "Warrior and Mage should have different stats"
        
        warrior_rogue_different = (
            warrior.health != rogue.health or
            warrior.strength != rogue.strength or
            warrior.magic != rogue.magic
        )
        assert warrior_rogue_different, "Warrior and Rogue should have different stats"

    def test_mages_are_more_magical(self):
        """Test that mages have higher magic than warriors"""
        warrior = Warrior("MagicWarrior")
        mage = Mage("MagicMage")
        
        assert mage.magic > warrior.magic, "Mages should have more magic than warriors"

    def test_warriors_are_tougher(self):
        """Test that warriors have higher health than mages"""
        warrior = Warrior("ToughWarrior")
        mage = Mage("ToughMage")
        
        assert warrior.health > mage.health, "Warriors should have more health than mages"

    def test_appropriate_stat_ranges(self):
        """Test that character stats are in reasonable ranges"""
        warrior = Warrior("RangeWarrior")
        mage = Mage("RangeMage")
        rogue = Rogue("RangeRogue")
        
        # Test reasonable stat ranges
        for char in [warrior, mage, rogue]:
            assert 50 <= char.health <= 200, f"{type(char).__name__} health should be reasonable"
            assert 5 <= char.strength <= 30, f"{type(char).__name__} strength should be reasonable"
            assert 0 <= char.magic <= 30, f"{type(char).__name__} magic should be reasonable"
