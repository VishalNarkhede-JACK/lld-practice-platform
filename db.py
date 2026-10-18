from models import Problem

PROBLEMS_DB = [
    Problem(
        id="p1", 
        title="Design a Parking Lot", 
        description="Design an automated parking lot system for motorcycles, cars, and buses.",
        requirements=[
            "Multiple floors and spot types",
            "Ticketing upon entry with timestamp",
            "Fee calculation upon exit based on vehicle type and duration",
            "Real-time spot availability display"
        ]
    ),
    Problem(
        id="p2", 
        title="Design an Elevator System", 
        description="Design the control system for a 10-story building with 3 elevators.",
        requirements=[
            "Internal floor selection buttons",
            "External hall call buttons (Up/Down)",
            "Elevator dispatch algorithm to minimize wait time",
            "Door open/close state and weight limit safety checks"
        ]
    ),


    Problem(
        id="p3",
        title="Design an Action RPG Combat System",
        description="Design a combat and character stat system where a player allocates stats (Strength, Dexterity) and fights bosses with multi-phase mechanics.",
        requirements=[
            "Player character class managing health, stamina, and stat attributes",
            "Weapon equip system with damage scaling based on player stats",
            "State machine for boss encounters (e.g., transitioning to a harder Phase 2 at 50% health)",
            "Damage calculation factoring in weapon types, player stats, and enemy defense"
        ]
    ),
    Problem(
        id="p4",
        title="Design an FPS Weapon Arsenal & Level Secrets",
        description="Design a fast-paced shooter's inventory system and level manager that handles quick weapon switching and secret item discovery.",
        requirements=[
            "Weapon arsenal allowing quick-switching between different weapon types (e.g., Shotgun, Plasma Rifle) sharing different ammo pools",
            "Level navigation manager tracking player coordinates and area progression",
            "Trigger system for discovering hidden areas and unlocking secret items",
            "Combat rating system that grades the player based on damage dealt and speed"
        ]
    ),
    Problem(
        id="p5",
        title="Design an RPG Bonding & Narrative Choice System",
        description="Design a dialogue and relationship system where player choices impact narrative branches and companion bond levels.",
        requirements=[
            "Dialogue tree structure handling branching conversations",
            "Companion entities tracking individual relationship/bonding points",
            "Event system that unlocks specific romance or narrative options when bond thresholds are met",
            "Save/Load state management for current dialogue progression and relationship status"
        ]
    )
]

SUBMISSIONS_DB = {}
EVALUATIONS_DB = {}