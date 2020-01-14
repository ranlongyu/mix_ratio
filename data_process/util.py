from main_app.model import Mix_ratio_table as Mix
from main_app import db


def store(data):
    for row in data:
        new_mix = Mix(
            mix_period=row["mix_period"],
            mix_concrete_variety=row["mix_concrete_variety"],
            mix_power_level=row["mix_power_level"],
            mix_impermeability_rating=row["mix_impermeability_rating"],
            mix_material_requirements=row["mix_material_requirements"],
            mix_limit_expansion_rate=row["mix_limit_expansion_rate"],
            mix_slump=row["mix_slump"],
            mix_expansion=row["mix_expansion"],

            mix_cement_consumption=row["mix_cement_consumption"],
            mix_special_fine_sand_dosage=row["mix_special_fine_sand_dosage"],
            mix_medium_sand_consumption=row["mix_medium_sand_consumption"],
            mix_coarse_sand_consumption=row["mix_coarse_sand_consumption"],
            mix_small_stone_dosage=row["mix_small_stone_dosage"],
            mix_big_stone_dosage=row["mix_big_stone_dosage"],
            mix_water_reducing_agent_dosage=row["mix_water_reducing_agent_dosage"],
            mix_fly_ash_dosage=row["mix_fly_ash_dosage"],
            mix_slag_powder_consumption=row["mix_slag_powder_consumption"],
            mix_limestone_powder_consumption=row["mix_limestone_powder_consumption"],
            mix_expansion_agent_dosage=row["mix_expansion_agent_dosage"],
            mix_water_consumption=row["mix_water_consumption"],
            mix_apparent_density=row["mix_apparent_density"],

            mix_production_workshop=row["mix_production_workshop"],
            mix_main_workshop=row["mix_main_workshop"],
            mix_production_line=row["mix_production_line"],
            mix_pouring_method=row["mix_pouring_method"],
            mix_3d_intensity=row["mix_3d_intensity"],
            mix_7d_intensity=row["mix_7d_intensity"],
            mix_28d_strength=row["mix_28d_strength"],
            mix_60d_strength=row["mix_60d_strength"],

            # mix_cement_sample_number = row[],
            cement_breed_grade=row["cement_breed_grade"],
            cement_28d_compression=row["cement_28d_compression"],
            cement_supply_unit=row["cement_supply_unit"],

            # mix_reduce_water_agent_sample_number = row[],
            reduce_breed_grade=row["reduce_breed_grade"],
            reduce_recommended_dosage=row["reduce_recommended_dosage"],
            reduce_water_reduction_rate=row["reduce_water_reduction_rate"],
            reduce_gas_content=row["reduce_gas_content"],
            reduce_28d_compressive_strength_ratio=row["reduce_28d_compressive_strength_ratio"],
            reduce_bleeding_rate_ratio=row["reduce_bleeding_rate_ratio"],

            # mix_fly_ash_sample_number = row[],
            fly_sample_category=row["fly_sample_category"],
            fly_breed_grade=row["fly_breed_grade"],
            fly_fineness=row["fly_fineness"],
            fly_water_demand_ratio=row["fly_water_demand_ratio"],
            fly_loss_on_ignition=row["fly_loss_on_ignition"],
            fly_activity_index=row["fly_activity_index"],

            # mix_slag_powder_sample_number = row[],
            slag_breed_grade=row["slag_breed_grade"],
            slag_28d_activity_index=row["slag_28d_activity_index"],
            slag_supply_unit=row["slag_supply_unit"],

            # mix_limestone_powder_sample_number = row[],
            limestone_fineness=row["limestone_fineness"],
            limestone_methylene_blue_value=row["limestone_methylene_blue_value"],
            limestone_28d_activity_index=row["limestone_28d_activity_index"],

            # mix_expansion_agent_sample_number = row[],
            expansion_breed_grade=row["expansion_breed_grade"],
            expansion_28d_compressive_strength=row["expansion_28d_compressive_strength"],
            expansion_limit_expansion_rate=row["expansion_limit_expansion_rate"]
        )
        db.session.add(new_mix)
        db.session.commit()
