# In this file we find the values of periodic orbits of order 27, winding number 11, for the hex billiard.
import pickle
import mpmath as mp
import general_lib
import billiard_hex

mp.mp.dps = 100
num_iter = 27


def error_iteration(phi: mp.mpf, p: mp.mpf) -> tuple:
    """Returns the difference between the original point and the 12 iterations of the billiard on it"""
    iteration_result = general_lib.iterate_function(
        general_lib.reflect_line_at_boundary, (phi, p), num_iter=num_iter,
        parametric_boundary=billiard_hex.param_boundary)[num_iter]
    return iteration_result[0] - phi, iteration_result[1] - p


initial_values = (mp.mpf(0.06), mp.mpf(0.48))  # Taken from the plots near this point
root = mp.findroot(error_iteration, initial_values, tol=mp.mpf(10) ** (-1.5 * mp.mp.dps), maxsteps=10)
root = (root[0], root[1])
periodic_orbit = general_lib.iterate_function(
        general_lib.reflect_line_at_boundary, root, num_iter=num_iter,
        parametric_boundary=billiard_hex.param_boundary)
print(mp.nstr(periodic_orbit, n=mp.mp.dps).replace("), (", "),\n("))
# [(0.06476110409861977000798282156400487942007420172751891371658770793934349638034729555230663606995758569,
# 0.4806888855137035248856951271028432034551375546698632423532296098224659322007937579040439578696080792),
# (2.617993877991494365385536152732919070164307832812588184145787160256513671905174165523362354451764223,
# 0.5218264629861932754282825037388687835354846649202267982120732996441893854984298452503700784708943528),
# (5.171226651884368960763089483901833260908541463897657454574986612573683847430001035494418072833570861,
# 0.4806888855137035248856951271028432034551375546698632423532296098224659322007937579040439578696080792),
# (1.446063893701486290569340261083821161241327487718681680363020960826834569568116298369155285609020538,
# 0.512448351532304886970902848525857171034215654030883021491213016804470674091810780850661068111072474),
# (4.004621001107966764107397586619296861574530179310485694697979137639356649581167727757139991335462259,
# 0.4826238273574219078740488139617858196019672520869658379166842652073014610577446095540293005368293426),
# (0.289107045605211026991251893065539676222593077225977563239349710867312905868579561205381633154819673,
# 0.4938015245654762991714482544333435386584428288938435355265692688837258573040561411892365661830934889),
# (2.852485607984582211471391490213963207974576322149128257735594881440503500417629437422653192187297395,
# 0.4938015245654762991714482544333435386584428288938435355265692688837258573040561411892365661830934889),
# (5.420156959661412951280532563219211791016978018814831768226854639284092569277459268126964484690888944,
# 0.4826238273574219078740488139617858196019672520869658379166842652073014610577446095540293005368293426),
# (1.69552875988830694789330312219568172295584191165642414061192363148098183671809270025887953973309653,
# 0.512448351532304886970902848525857171034215654030883021491213016804470674091810780850661068111072474),
# (4.253551308885010754624840665936675391682966734227660008349847164349765371428625960389686403192780343,
# 0.4806888855137035248856951271028432034551375546698632423532296098224659322007937579040439578696080793),
# (0.5235987755982988730771072305465838140328615665625176368291574320513027343810348331046724708903528444,
# 0.5218264629861932754282825037388687835354846649202267982120732996441893854984298452503700784708943527),
# (3.076831549491173468454660561715498004777095197647586907258356884368472909905861703075728189272159482,
# 0.4806888855137035248856951271028432034551375546698632423532296098224659322007937579040439578696080793),
# (5.634854098487877275186198105456491673504220020218822774996280417237256444616394963206535052731843295,
# 0.512448351532304886970902848525857171034215654030883021491213016804470674091810780850661068111072474),
# (1.91022589871477127179896866443296160544308391306041514738134940943414571205702839533845010777405088,
# 0.4826238273574219078740488139617858196019672520869658379166842652073014610577446095540293005368293428),
# (4.47789725039160201160810973743821018848548560972611865787260916727773478091685822604276140027764243,
# 0.493801524565476299171448254433343538658442828893843535526569268883725857304056141189236566183093489),
# (0.7580905055913867191629625680276279518431300558990577104189651532352925628934901050039633086258860155,
# 0.4938015245654762991714482544333435386584428288938435355265692688837258573040561411892365661830934892),
# (3.325761857268217458972103641032876534885531752564761220910224911078881631753319935708274601129477565,
# 0.4826238273574219078740488139617858196019672520869658379166842652073014610577446095540293005368293428),
# (5.884318964674697932510160966568352235218734444156565235245183087891403711766371365096259306855919286,
# 0.5124483515323048869709028485258571710342156540308830214912130168044706740918107808506610681110724743),
# (2.159156206491815262316411743750340135551520467977589461033217436144554433904486627970996519631368963,
# 0.4806888855137035248856951271028432034551375546698632423532296098224659322007937579040439578696080793),
# (4.7123889803846898576939650749192543262957540990626587314624168884617246094293134979420522380131756,
# 0.5218264629861932754282825037388687835354846649202267982120732996441893854984298452503700784708943528),
# (0.9824364470979779761462316395291627486456489313975163599417271561632619723817223706570383057107481019,
# 0.4806888855137035248856951271028432034551375546698632423532296098224659322007937579040439578696080794),
# (3.540458996094681782877769183270156417372773753968752227679650689032045507092255630787845169170431915,
# 0.5124483515323048869709028485258571710342156540308830214912130168044706740918107808506610681110724738),
# (6.099016103501162256415826508805632117705976445560556242014608865844567587105307060175829874896873636,
# 0.4826238273574219078740488139617858196019672520869658379166842652073014610577446095540293005368293428),
# (2.38350214799840651929968081525187493235403934347604811055597943907252384339271889362407151671623105,
# 0.4938015245654762991714482544333435386584428288938435355265692688837258573040561411892365661830934888),
# (4.946880710377777703779820412400298464106022588399198805052224609645714437941768769841343075748708771,
# 0.4938015245654762991714482544333435386584428288938435355265692688837258573040561411892365661830934895),
# (1.231366754875021966663674718846541278754085486314690673593595182873670694229180603289584717568066185,
# 0.4826238273574219078740488139617858196019672520869658379166842652073014610577446095540293005368293428),
# (3.789923862281502440201732044382016979087288177906494687928553359686192774242232032677569423294507906,
# 0.5124483515323048869709028485258571710342156540308830214912130168044706740918107808506610681110724747),
# (0.06476110409861977000798282156400487942007420172751891371658770793934349638034729555230663606995758184,
# 0.4806888855137035248856951271028432034551375546698632423532296098224659322007937579040439578696080795)]

initial_phi = root[0]
initial_p = root[1]

orbit = general_lib.calculate_orbit(parametric_boundary=billiard_hex.param_boundary, initial_phi=initial_phi,
                                    initial_p=initial_p, num_iterations=num_iter)

filename = f"orbits_hex/singular_orbit_11_27_prec100.pkl"
with open(filename, "wb") as file:
    pickle.dump(orbit, file)
print(f"Created {filename}")
# Created orbits_hex/singular_orbit_11_27_prec100.pkl
