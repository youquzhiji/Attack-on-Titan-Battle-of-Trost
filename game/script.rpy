# 游戏的脚本可置于此文件中。
define armin=Character("阿尔敏")
define n=Character("旁白")
default survive=[0,0,0,0,0,0,0,0,0,0]
default unlockedclues=[0,0,0]
define arminindex=0
init python:

    def generateclue(gatheredclues):
        result=""
        if gatheredclues[0]==1:
            result+="noticed annie's feeling\n"
        if gatheredclues[1]==1:
            result+="find a horse from remoos company\n"
        if gatheredclues[2]==1:
            result+="found a way to communicate with survey corp\n"
        return result
    def puzzle(playerinput, rightanswer,previouschoice):
        if(playerinput == rightanswer):
            renpy.jump("chapter_" + rightanswer)
        else:
            while(playerinput!=rightanswer):
                n("错误,输入quit退出或重试")
                playerinput=renpy.input("你的新答案").strip()
                if(playerinput == rightanswer):
                    renpy.jump("chapter_" + rightanswer)
                elif(playerinput=="quit"):
                    renpy.jump(previouschoice)

            return
    config.rollback_enabled=False
    def digit(playerinput,rightanswer):
        if(playerinput==rightanswer):
            return TRUE
        else:
            return FALSE

        ##todo 根据角色生还状态和线索显示菜单
    def displayTitanRoster(previousplace,rightanswer):
#TODO 如果玩家选择输入数字
#TODO:如果玩家点击返回
        renpy.jump ("chapter_"+previousplace)
        return
# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

#    python:
#        answer = renpy.input("What is your name?")
#        answer = povname.strip()
#        puzzle(answer,"315")


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    show eileen happy


    # 此处显示各行对话。
    #巨人吃人图
    n "世界已经被巨人占领了。"
    #三堵墙鸟瞰图
    n "沦为了这些巨大生物饲料的人类，修建了三座大墙，在墙内维持着脆弱的和平和秩序。"
    #黑色
    n "但是五年前，在 845年......"
    #超巨探头
    ##巨人出现音乐
    n "超大型巨人出现，随后，人类的第一堵墙，玛利亚之墙被破坏。"

    n "一个世纪以来的和平终结了。人类失去了三分之一的土地和三分之一的人口。"
    #黑屏 850数字
    n "现在——850年。"

    n "在人类的第二堵墙最南侧的特罗斯特街区，超大型巨人，第二次出现。"

    n "为了不让玛利亚之墙的悲剧重演，为了保护人类仅存的领土，人类必须要不惜一切代价保卫罗塞之墙。"

    n "但是......"

    n "战斗经验最为丰富的调查兵团正在进行壁外调查。这次战斗的责任落到了驻屯兵团......和一群刚刚毕业的训练兵们的肩上。"

    n "你是104期训练兵中的一个无名士兵，你的选择会影响故事的走向。"
    n "一个错误的选择就可能导致死亡，或者是人类的失败。"
    n "然而，经过仔细的判断，你也许能为人类的胜利做出贡献，甚至让原作中的角色免于一死。"

    jump chapter_1

label chapter_1:
    show ct
    n "半空中出现了一副巨大的面孔。"
    n "它虽然有着人类的形状，但是没有皮肤，鲜红的肌肉完全暴露在空气之中。"
    n "你还没来得及去注意它奇怪的样子，就被一股强大的气浪击中了。"
    #白屏幕
    n "巨浪吹走了你，而你的视野变成了一片白色。"
    n "此时此刻，你的大脑如同你的视野一样空白。有那么一秒，你甚至搞不清现在到底是怎么回事。"
    # 蓝天
    n "你被抛到了半空中，离地面足足有50米。头上的蓝天意外地平静，而地上那些发红的屋顶看起来，就像玩具一样小。"

label chapter_2:
    n "你现在正在50米的高空中，不过不会持续太久。你现在怎么做？"
    menu:
        "找东西抓住":
            jump chapter_3
        "用气体推动身体":
            jump chapter_4
        "用立体机动装置的固定器勾住墙壁":
            jump chapter_5
label chapter_3:
    #黑屏
    n "你没在天上找到可以抓的地方。离你几米之外有一堵大墙，但是你不管怎么伸手也够不到。"
    n "你摔死了。"
    menu:
        "重试":
            jump chapter_2
label chapter_4:
##黑色
    n "你让大腿旁的机器喷出了一些气体......但是没能减缓你下坠的速度。"
    n "也许更有经验的人用这些气体轻微地改变一下角度，但是并不能阻止掉落。"
    n "更有经验.......更有什么经验来着？"
    n "在你能想起来之前，你重重地摔在了地上。"
    n"你死了。"
    menu:
        "重试":
            jump chapter_2
label chapter_5:
    n "立体机动装置是什么？固定器又是什么？"
    n "你可能已经忘记了，但是你的身体还记得。"
    n "你立刻从身边的皮质盒子里取出了手枪一样的控制装备，转向墙壁并扣下了扳机。"
    n "身体两侧的发射器射出了如同标枪一样的东西，扎进了墙壁里，连接固定器的缆绳阻止了你的坠落。"
    #第一人称视角踩墙
    n "你现在挂在了墙上。接着你扣下了扳机，放出了压缩气体，缆绳开始收紧，借助这股力量，你的脚踩到了墙，并开始攀爬。"
    n "你想起来了：你可以用一种一般人想也不敢想的方式控制你在空中的位置。你靠在缆绳上。这是三年训练的成果。"
    jump chapter_6
label chapter_6:
    n "这是你第一次看到这些吗？"
    menu chapter_6_choice:
        "是（阅读新手教程）":
            jump chapter_7
        "否":
            jump chapter_96
label chapter_7:
    #黑屏
    n "你想起来了，你是104期训练兵团特罗斯特训练营的一员，位于罗塞之墙最南侧。"
    n "罗塞之墙东南西北四个方向都有训练营，而南侧是离前线最近的街区。"
    n "经过了三年的艰苦训练，你和你的同学们正处于毕业后等待——至少曾经是在等待选择自己要加入兵团。"
    n "为什么要是现在？"
    n "你回想起来，几个小时前，特罗斯特街区还是很和平的样子。"
    n "*如何游玩本作*"
    n "你将扮演一名104期训练兵，与你的同学们一起战斗，其中包括艾伦和三笠。"
    n "本作是一个平行世界：如果你当时在场，世界会变成什么样子？"
    n "*战斗报告*"
    n "下方的菜单中有一个选项会打开站战斗报告，上边会记录你获得的线索和物品。"
    n "*同伴和亲密度*"
    n "战斗报告还会列出和你一同战斗的战友，包括104期的同学和其他士兵。"
    n "同时，战斗报告还会记录角色的阵亡情况，死去的角色会被红色的叉标记。"
    n "随着故事的进展，你会和部分角色产生不同程度的亲密度，这点也会在战斗报告中表现出来。"
    n "*谜题*"
    n "本作中有很多谜题需要解开，找到正确答案的话可以开启不同的选项。"
    n "如果你能找到正确答案，那么证明你对战场的状态观察的很仔细。"
    n "*不同的结局*"
    n "基于你的选择，故事可能会走向更坏的方向，也有可能走向更好的方向，如果你能成功解谜的话，甚至能让有些角色免于一死。"
    n "以上就是对于本游戏的说明，是否要阅读现在可公开的信息？"
    menu:
        "是":
            jump chapter_8
        "否":
            jump chapter_9
label chapter_8:
    n "烂大街情报"
    #动画风格绘画最好
    ##无脑巨
    #奇行种
    #巨人习性
    #立体机动装置
label chapter_9:
    #街景
    ##真转4米卡多风格音乐
    n "你现在正在特罗斯特街区行走。"
    n "你是104期训练兵团特罗斯特训练营的一员，这三年你一直在城外的地方训练。"
    n "特罗斯特街区是罗塞之墙的最南端，人类防御的第一线。你的训练营一直认为，在同期一个八个训练营中，自己是最精锐的。"
    n "你还记得五年前的惨剧。超大型巨人的攻击和玛利亚之墙的沦陷。人类不得不退缩至领土深处，并且因此损失了20%的人口。"
    n "你当时还是个孩子。而五年前的惨剧就是你加入训练兵团的原因。三年的训练艰苦而残酷，但是有不少好同学。"
    #艾伦训练成功
    #三笠立体机动装置林间飞行
    #阿明和三人组热切交流
    #马可和维护立体机动装置
    #莱纳扛木头
    #阿尼冷漠泰拳姿势
    #科尼莎夏功夫
    #贝贝奇怪睡姿
    #让让子艾伦打架，情侣秀恩爱
label chapter_10:
label chapter_11:
label chapter_12:
label chapter_13:
label chapter_14:
label chapter_15:
label chapter_16:
label chapter_17:
label chapter_18:
label chapter_19:
label chapter_20:
label chapter_21:
label chapter_22:
label chapter_23:
label chapter_24:
label chapter_25:
label chapter_26:
label chapter_27:
label chapter_28:
label chapter_29:
label chapter_30:
label chapter_31:
label chapter_32:
label chapter_33:
label chapter_34:
label chapter_35:
label chapter_36:
label chapter_37:
label chapter_38:
label chapter_39:
label chapter_40:
label chapter_41:
label chapter_42:
label chapter_43:
label chapter_44:
label chapter_45:
label chapter_46:
label chapter_47:
label chapter_48:
label chapter_49:
label chapter_50:
label chapter_51:
label chapter_52:
label chapter_53:
label chapter_54:
label chapter_55:
label chapter_56:
label chapter_57:
label chapter_58:
label chapter_59:
label chapter_60:
label chapter_61:
label chapter_62:
label chapter_63:
label chapter_64:
label chapter_65:
label chapter_66:
label chapter_67:
label chapter_68:
label chapter_69:
label chapter_70:
label chapter_71:
label chapter_72:
label chapter_73:
label chapter_74:
label chapter_75:
label chapter_76:
label chapter_77:
label chapter_78:
label chapter_79:
label chapter_80:
label chapter_81:
label chapter_82:
label chapter_83:
label chapter_84:
label chapter_85:
label chapter_86:
label chapter_87:
label chapter_88:
label chapter_89:
label chapter_90:
label chapter_91:
label chapter_92:
label chapter_93:
label chapter_94:
label chapter_95:
label chapter_96:
label chapter_97:
label chapter_98:
label chapter_99:
label chapter_100:
label chapter_101:
label chapter_102:
label chapter_103:
label chapter_104:
label chapter_105:
label chapter_106:
label chapter_107:
label chapter_108:
label chapter_109:
label chapter_110:
label chapter_111:
label chapter_112:
label chapter_113:
label chapter_114:
label chapter_115:
label chapter_116:
label chapter_117:
label chapter_118:
label chapter_119:
label chapter_120:
label chapter_121:
label chapter_122:
label chapter_123:
label chapter_124:
label chapter_125:
label chapter_126:
label chapter_127:
label chapter_128:
label chapter_129:
label chapter_130:
label chapter_131:
label chapter_132:
label chapter_133:
label chapter_134:
label chapter_135:
label chapter_136:
label chapter_137:
label chapter_138:
label chapter_139:
label chapter_140:
label chapter_141:
label chapter_142:
label chapter_143:
label chapter_144:
label chapter_145:
label chapter_146:
label chapter_147:
label chapter_148:
label chapter_149:
label chapter_150:
label chapter_151:
label chapter_152:
label chapter_153:
label chapter_154:
label chapter_155:
label chapter_156:
label chapter_157:
label chapter_158:
label chapter_159:
label chapter_160:
label chapter_161:
label chapter_162:
label chapter_163:
label chapter_164:
label chapter_165:
label chapter_166:
label chapter_167:
label chapter_168:
label chapter_169:
label chapter_170:
label chapter_171:
label chapter_172:
label chapter_173:
label chapter_174:
label chapter_175:
label chapter_176:
label chapter_177:
label chapter_178:
label chapter_179:
label chapter_180:
label chapter_181:
label chapter_182:
label chapter_183:
label chapter_184:
label chapter_185:
label chapter_186:
label chapter_187:
label chapter_188:
label chapter_189:
label chapter_190:
label chapter_191:
label chapter_192:
label chapter_193:
label chapter_194:
label chapter_195:
label chapter_196:
label chapter_197:
label chapter_198:
label chapter_199:
label chapter_200:
label chapter_201:
label chapter_202:
label chapter_203:
label chapter_204:
label chapter_205:
label chapter_206:
label chapter_207:
label chapter_208:
label chapter_209:
label chapter_210:
label chapter_211:
label chapter_212:
label chapter_213:
label chapter_214:
label chapter_215:
label chapter_216:
label chapter_217:
label chapter_218:
label chapter_219:
label chapter_220:
label chapter_221:
label chapter_222:
label chapter_223:
label chapter_224:
label chapter_225:
label chapter_226:
label chapter_227:
label chapter_228:
label chapter_229:
label chapter_230:
label chapter_231:
label chapter_232:
label chapter_233:
label chapter_234:
label chapter_235:
label chapter_236:
label chapter_237:
label chapter_238:
label chapter_239:
label chapter_240:
label chapter_241:
label chapter_242:
label chapter_243:
label chapter_244:
label chapter_245:
label chapter_246:
label chapter_247:
label chapter_248:
label chapter_249:
label chapter_250:
label chapter_251:
label chapter_252:
label chapter_253:
label chapter_254:
label chapter_255:
label chapter_256:
label chapter_257:
label chapter_258:
label chapter_259:
label chapter_260:
label chapter_261:
label chapter_262:
label chapter_263:
label chapter_264:
label chapter_265:
label chapter_266:
label chapter_267:
label chapter_268:
label chapter_269:
label chapter_270:
label chapter_271:
label chapter_272:
label chapter_273:
label chapter_274:
label chapter_275:
label chapter_276:
label chapter_277:
label chapter_278:
label chapter_279:
label chapter_280:
label chapter_281:
label chapter_282:
label chapter_283:
label chapter_284:
label chapter_285:
label chapter_286:
label chapter_287:
label chapter_288:
label chapter_289:
label chapter_290:
label chapter_291:
label chapter_292:
label chapter_293:
label chapter_294:
label chapter_295:
label chapter_296:
label chapter_297:
label chapter_298:
label chapter_299:
    n "not quite"
    return
label chapter_300:
label chapter_301:
label chapter_302:
label chapter_303:
label chapter_304:
label chapter_305:
label chapter_306:
label chapter_307:
label chapter_308:
label chapter_309:
label chapter_310:
label chapter_311:
label chapter_312:
label chapter_313:
label chapter_314:
label chapter_315:
    n "glad you made it"

# 此处为游戏结尾。

    return
