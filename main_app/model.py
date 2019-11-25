from main_app import db  # db是在main_app/__init__.py生成的关联后的SQLAlchemy实例

class Mix_ratio_table(db.Model):
    __tablename__ = '混凝土配合比'
    id = db.Column(db.BigInteger, primary_key=True)
    mix_period = db.Column(db.Float(), comment='小票时间月份')
    mix_concrete_variety = db.Column(db.String(128), comment='混凝土品种')
    mix_power_level = db.Column(db.String(128), comment='强度等级')
    mix_impermeability_rating = db.Column(db.String(128), comment='抗渗等级')
    mix_material_requirements = db.Column(db.String(128), comment='材料要求')
    mix_limit_expansion_rate = db.Column(db.Float(), comment='限制膨胀率')
    mix_slump = db.Column(db.Float(), comment='塌落度')
    mix_expansion = db.Column(db.Float(), comment='扩展度')

    mix_cement_consumption = db.Column(db.Float(), comment='水泥用量')
    mix_special_fine_sand_dosage = db.Column(db.Float(), comment='特细砂用量')
    mix_medium_sand_consumption = db.Column(db.Float(), comment='中砂用量')
    mix_coarse_sand_consumption = db.Column(db.Float(), comment='粗砂用量')
    mix_small_stone_dosage = db.Column(db.Float(), comment='小石用量')
    mix_big_stone_dosage = db.Column(db.Float(), comment='大石用量')
    mix_water_reducing_agent_dosage = db.Column(db.Float(), comment='减水剂用量')
    mix_fly_ash_dosage = db.Column(db.Float(), comment='粉煤灰用量')
    mix_slag_powder_consumption = db.Column(db.Float(), comment='矿渣粉用量')
    mix_limestone_powder_consumption = db.Column(db.Float(), comment='石灰石粉用量')
    mix_expansion_agent_dosage = db.Column(db.Float(), comment='膨胀剂用量')
    mix_water_consumption = db.Column(db.Float(), comment='水用量')
    mix_apparent_density = db.Column(db.Float(), comment='表观密度')

    mix_production_workshop = db.Column(db.String(128), comment='生产车间')
    mix_main_workshop = db.Column(db.String(128), comment='主供车间')
    mix_production_line = db.Column(db.String(128), comment='生产线')
    mix_pouring_method = db.Column(db.String(128), comment='浇注方式')
    mix_3d_intensity = db.Column(db.Float(), comment='3d强度')
    mix_7d_intensity = db.Column(db.Float(), comment='7d强度')
    mix_28d_strength = db.Column(db.Float(), comment='28d强度')
    mix_60d_strength = db.Column(db.Float(), comment='60d强度')

    # mix_cement_sample_number = db.Column(db.String(128), comment='水泥样品编号')
    cement_breed_grade = db.Column(db.String(128), comment='品种等级')
    cement_28d_compression = db.Column(db.Float(), comment='28d抗压')
    cement_supply_unit = db.Column(db.String(128), comment='供应单位')

    # mix_reduce_water_agent_sample_number = db.Column(db.String(128), comment='减水剂样品编号')
    reduce_breed_grade = db.Column(db.String(128), comment='品种等级')
    reduce_recommended_dosage = db.Column(db.Float(), comment='推荐掺量')
    reduce_water_reduction_rate = db.Column(db.Float(), comment='减水率')
    reduce_gas_content = db.Column(db.Float(), comment='含气量')
    reduce_28d_compressive_strength_ratio = db.Column(db.Float(), comment='28d抗压强度比')
    reduce_bleeding_rate_ratio = db.Column(db.Float(), comment='泌水率比')

    # mix_fly_ash_sample_number = db.Column(db.String(128), comment='粉煤灰样品编号')
    fly_sample_category = db.Column(db.String(128), comment='样品类别')
    fly_breed_grade = db.Column(db.String(128), comment='品种等级')
    fly_fineness = db.Column(db.Float(), comment='细度')
    fly_water_demand_ratio = db.Column(db.Float(), comment='需水量比')
    fly_loss_on_ignition = db.Column(db.Float(), comment='烧失量')
    fly_activity_index = db.Column(db.Float(), comment='活性指数')

    # mix_slag_powder_sample_number = db.Column(db.String(128), comment='矿渣粉样品编号')
    slag_breed_grade = db.Column(db.String(128), comment='品种等级')
    slag_28d_activity_index = db.Column(db.Float(), comment='28d活性指数')
    slag_supply_unit = db.Column(db.String(128), comment='供应单位')

    # mix_limestone_powder_sample_number = db.Column(db.String(128), comment='石灰石粉样品编号')
    limestone_fineness = db.Column(db.Float(), comment='细度')
    limestone_methylene_blue_value = db.Column(db.Float(), comment='亚甲蓝值')
    limestone_28d_activity_index = db.Column(db.Float(), comment='28d活性指数')

    # mix_expansion_agent_sample_number = db.Column(db.String(128), comment='膨胀剂样品编号')
    expansion_breed_grade = db.Column(db.String(128), comment='品种等级')
    expansion_28d_compressive_strength = db.Column(db.Float(), comment='28d抗压强度')
    expansion_limit_expansion_rate = db.Column(db.Float(), comment='限制膨胀率')

    # __repr__方法用于在调试时打印实例
    def __repr__(self):
        return '<Mix_ratio_table %r>' % self.id
