#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def translate_html_file(file_path):
    """翻译HTML文件中的英文内容为中文"""
    
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义翻译映射
    translations = {
        # 标题和导航
        'Zhongyi Lianyungang': '连云港中意航空材料有限公司',
        'ZhongYi': '中意',
        'Home': '首页',
        'About': '关于我们',
        'Machines': '设备',
        'Abrasives': '磨料',
        'Contact us': '联系我们',
        'Search': '搜索',
        'Our Products': '我们的产品',
        'Get In touch': '联系我们',
        
        # 联系信息
        'Lianyungang, China': '中国连云港',
        'Call : +86-15825595194': '电话：+86-15825595194',
        'Add:No.9, Lingang Industry Area, Guanyun, Lianyungang, Jiangsu, China. P.C.:222200': '地址：中国江苏省连云港市灌云县临港产业区9号。邮编：222200',
        'Email: mancy@zylyg.com': '邮箱：mancy@zylyg.com',
        'Mobile: 86-15825595194': '手机：86-15825595194',
        'Tel: 86-518-85289056': '电话：86-518-85289056',
        'Fax: 86-518-88987316': '传真：86-518-88987316',
        'Contact Us': '联系我们',
        'PRODUCTS': '产品',
        
        # 产品名称
        'Urea Blast Media': '尿素喷砂磨料',
        'Glass beads': '玻璃珠',
        'Brown Fused Alumina': '棕刚玉',
        'Silicon Carbide': '碳化硅',
        
        # 版权信息
        'Copyright &copy; 2025. ZhongYi All rights reserved.': '版权所有 &copy; 2025. 连云港中意航空材料有限公司 保留所有权利。',
        
        # 产品详情页面的特定翻译
        'Type II Urea Blast Media': 'II型尿素喷砂磨料',
        'Type III Melamine Blast Media': 'III型三聚氰胺喷砂磨料',
        'Glass Beads': '玻璃珠',
        'Brown Fused Alumina': '棕刚玉',
        'White Fused Alumina': '白刚玉',
        'Silicon Carbide': '碳化硅',
        'Steel Shot': '钢丸',
        'Steel Grit': '钢砂',
        'Cut Wire Shot': '钢丝切丸',
        'Aluminum Oxide': '氧化铝',
        
        # 技术参数
        'Project': '项目',
        'Technical index': '技术指标',
        'Type': '类型',
        'Chlorine content': '氯含量',
        'PH value': 'PH值',
        'Conductivity(us/cm)': '电导率(us/cm)',
        'Bulk density (g/cm³)': '堆积密度 (g/cm³)',
        'Color': '颜色',
        'White or Multicolor Blending': '白色或多色混合',
        'Babbit hardness (HB a)': '巴氏硬度 (HB a)',
        'Qualitative analysis': '定性分析',
        'Urea formaldehyde resin': '脲醛树脂',
        'Melamine resin': '三聚氰胺树脂',
        'Paint removal rate': '除漆率',
        'square foot/min': '平方英尺/分钟',
        'Initiative': '主动性',
        'mg/ Square centimetre': '毫克/平方厘米',
        'Consumption rate (one cycle)': '消耗率（一个周期）',
        'Granularity': '粒度',
        
        # 产品特性
        'Types of Plastic Abrasive': '塑料磨料类型',
        'We offer two forms of Plastic Abrasive': '我们提供两种形式的塑料磨料',
        'Type II (Urea, which is hard and durable )': 'II型（尿素，坚硬耐用）',
        'Type III (Melamine, the hardest and the most aggressive of the plastic media)': 'III型（三聚氰胺，塑料磨料中最硬最激进的）',
        'Characteristics of Plastic Abrasive': '塑料磨料特性',
        'Sustainable': '可持续的',
        'Silica Free': '无硅',
        'High Effective Cost': '高效成本',
        'No Leftover': '无残留',
        'Angular and Lightweight Material': '角状轻质材料',
        'Applications of Plastic Abrasive': '塑料磨料应用',
        'Aerospace': '航空航天',
        'Tire Manufacturing': '轮胎制造',
        'Automotive Industry': '汽车工业',
        'Shoe Manufacturing': '鞋类制造',
        'Coating and Painting': '涂层和喷漆',
        'Plastic Abrasive Manufacturer in China': '中国塑料磨料制造商',
        
        # 产品描述
        'Plastic abrasive beads are commonly used for paint stripping, coatings removal, pressure blasting, powder coating, deflashing, deburring, surface preparation, and mold cleaning.': '塑料磨料珠常用于脱漆、涂层去除、压力喷砂、粉末涂料、去毛刺、表面处理和模具清洁。',
        'Plastic abrasive media is used for paint removal and refurbishing steel, aluminum, rubber, composites, cars, trucks, airplanes, helicopters, boats, and motorcycles.': '塑料磨料介质用于脱漆和翻新钢材、铝材、橡胶、复合材料、汽车、卡车、飞机、直升机、船只和摩托车。',
        'Plastic Abrasive is available in all standard sizes for deflashing & deburring applications: Cryogenic Deflashing Media, Polycarbonate, Nylon Polyamide, and Polystyrene Beads.': '塑料磨料提供所有标准尺寸，适用于去毛刺应用：低温去毛刺介质、聚碳酸酯、尼龙聚酰胺和聚苯乙烯珠。',
        'Blasting with Plastic Media avoids damage to delicate substrates thus a superb alternative to hard abrasive materials also as chemical stripping.': '使用塑料介质喷砂可避免损坏精密基材，因此是硬质磨料材料和化学剥离的绝佳替代品。',
        'Plastic abrasive is often reclaimed repeatedly, offering excellent cost benefits.': '塑料磨料通常可以重复回收利用，提供出色的成本效益。',
        
        # 制造商描述
        'We are Manufacturer, Supplier, and Exporter of Sand Blasting Machine, Tumblast Shot Blasting Machine Grit Blasting Machine, Thermal Spray Gun, Sand Blasting Cabinet, Shot Blasting Room, Pressure blasting Cabinet, Metalizing Gun in Jiangsu, China, China at low price with the best quality for Sale.': '我们是喷砂机、转鼓抛丸机、喷砂机、热喷涂枪、喷砂柜、抛丸室、压力喷砂柜、金属化枪的制造商、供应商和出口商，位于中国江苏，以低价提供最优质的产品。',
        'surface polishing Blast room believes that for any business quality is mandatory and we are committed to that.': '表面抛光喷砂室认为，对于任何企业来说，质量都是必须的，我们致力于此。',
        'Our main aim to satisfy our customers by giving them the best products and we are committed to our quality integrity and transparency of our business.': '我们的主要目标是通过提供最好的产品来满足客户，我们致力于质量诚信和业务透明度。',
        
        # 询价信息
        'To enable us to quote for your requirement, kindly give us the following info –': '为了能够为您的要求报价，请提供以下信息：',
        'Particle size required (You may choose from above or give your own range)': '所需粒度（您可以从上述选择或提供自己的范围）',
        'Packing required': '所需包装',
        'Quantity required with a delivery schedule.': '所需数量和交货时间表。',
        'Destination port': '目的港',
        'Payment terms.': '付款条件。',
        'Discharge rate at the destination, if in break-bulk.': '目的港卸货率（如果是散货）。',
        'Any other point which may impact the quote.': '可能影响报价的任何其他要点。',
        'We can also offer ungraded material for shipments in bulk in any quantities as desired by our buyers on FOB basis terms.': '我们还可以根据买家的要求，按FOB条款提供任何数量的散装未分级材料。',
    }
    
    # 应用翻译
    for english, chinese in translations.items():
        content = content.replace(english, chinese)
    
    # 特殊处理：翻译表格中的内容
    # 这里可以添加更多特定的翻译规则
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已翻译: {file_path}")

def main():
    """主函数：翻译所有产品页面"""
    
    # 产品页面文件列表
    product_files = [
        'product-1.html', 'product-2.html', 'product-3.html', 'product-4.html',
        'product-5.html', 'product-6.html', 'product-7.html', 'product-8.html',
        'product-9.html', 'product-10.html'
    ]
    
    # 设备页面文件列表
    machine_files = [
        'machine-1.html', 'machine-2.html', 'machine-3.html', 'machine-4.html',
        'machine-5.html', 'machine-6.html', 'machine-7.html', 'machine-8.html'
    ]
    
    # 翻译所有产品页面
    for file_name in product_files:
        if os.path.exists(file_name):
            translate_html_file(file_name)
        else:
            print(f"文件不存在: {file_name}")
    
    # 翻译所有设备页面
    for file_name in machine_files:
        if os.path.exists(file_name):
            translate_html_file(file_name)
        else:
            print(f"文件不存在: {file_name}")
    
    print("所有页面翻译完成！")

if __name__ == "__main__":
    main() 