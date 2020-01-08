from main_app.model import Mix_ratio_table as Mix
from main_app import db


def store(data):
    for row in data:
        new_mix = Mix(
            mix_period=row[0],
            mix_concrete_variety=row[1],
            mix_power_level=row[2],
            mix_impermeability_rating=row[3],
            mix_material_requirements=row[4],
            mix_limit_expansion_rate=row[5],
            mix_slump=row[6],
            mix_expansion=row[7],

            mix_cement_consumption=row[8],
            mix_special_fine_sand_dosage=row[9],
            mix_medium_sand_consumption=row[10],
            mix_coarse_sand_consumption=row[11],
            mix_small_stone_dosage=row[12],
            mix_big_stone_dosage=row[13],
            mix_water_reducing_agent_dosage=row[14],
            mix_fly_ash_dosage=row[15],
            mix_slag_powder_consumption=row[16],
            mix_limestone_powder_consumption=row[17],
            mix_expansion_agent_dosage=row[18],
            mix_water_consumption=row[19],
            mix_apparent_density=row[20],

            mix_production_workshop=row[21],
            mix_main_workshop=row[22],
            mix_production_line=row[23],
            mix_pouring_method=row[24],
            mix_3d_intensity=row[25],
            mix_7d_intensity=row[26],
            mix_28d_strength=row[27],
            mix_60d_strength=row[28],

            # mix_cement_sample_number = row[],
            cement_breed_grade=row[29],
            cement_28d_compression=row[30],
            cement_supply_unit=row[31],

            # mix_reduce_water_agent_sample_number = row[],
            reduce_breed_grade=row[32],
            reduce_recommended_dosage=row[33],
            reduce_water_reduction_rate=row[34],
            reduce_gas_content=row[35],
            reduce_28d_compressive_strength_ratio=row[36],
            reduce_bleeding_rate_ratio=row[37],

            # mix_fly_ash_sample_number = row[],
            fly_sample_category=row[38],
            fly_breed_grade=row[39],
            fly_fineness=row[40],
            fly_water_demand_ratio=row[41],
            fly_loss_on_ignition=row[42],
            fly_activity_index=row[43],

            # mix_slag_powder_sample_number = row[],
            slag_breed_grade=row[44],
            slag_28d_activity_index=row[45],
            slag_supply_unit=row[46],

            # mix_limestone_powder_sample_number = row[],
            limestone_fineness=row[47],
            limestone_methylene_blue_value=row[48],
            limestone_28d_activity_index=row[49],

            # mix_expansion_agent_sample_number = row[],
            expansion_breed_grade=row[50],
            expansion_28d_compressive_strength=row[51],
            expansion_limit_expansion_rate=row[52]
        )
        db.session.add(new_mix)
        db.session.commit()
