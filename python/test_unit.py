import numpy as np
import matrix as eigenpy

verbose = False

if verbose: print "===> From MatrixXd to Py"
M = eigenpy.naturals(3,3,verbose)
Mcheck = np.reshape(np.array(range(9),np.double),[3,3])
assert np.array_equal(Mcheck,M)

if verbose: print "===> From Matrix3d to Py"
M33= eigenpy.naturals33(verbose)
assert np.array_equal(Mcheck,M33)

if verbose: print "===> From VectorXd to Py"
v = eigenpy.naturalsX(3,verbose)
vcheck = np.array([range(3),],np.double).T
assert np.array_equal(vcheck ,v)

if verbose: print "===> From Py to Eigen::MatrixXd"
if verbose: print "===> From Py to Eigen::MatrixXd"
if verbose: print "===> From Py to Eigen::MatrixXd"
Mref = np.reshape(np.array(range(64),np.double),[8,8])

if verbose: print "===> Matrix 8x8"
M = Mref
assert( np.array_equal(M,eigenpy.reflex(M,verbose)) );

if verbose: print "===> Block 0:3x0:3"
M = Mref[0:3,0:3]
assert( np.array_equal(M,eigenpy.reflex(M,verbose)) );

if verbose: print "===> Block 1:3x1:3"
M = Mref[1:3,1:3]
assert( np.array_equal(M,eigenpy.reflex(M,verbose)) );

if verbose: print "===> Block 1:5:2x1:5:2"
M = Mref[1:5:2,1:5:2]
assert( np.array_equal(M,eigenpy.reflex(M,verbose)) );

if verbose: print "===> Block 1:8:3x1:5"
M = Mref[1:8:3,1:5]
assert( np.array_equal(M,eigenpy.reflex(M,verbose)) );

if verbose: print "===> Block transpose 1:8:3x1:6:2"
M = Mref[1:8:3,0:6:2].T
assert( np.array_equal(M,eigenpy.reflex(M,verbose)) );

if verbose: print "===> Block Vector 1x0:6:2"
M = Mref[1:2,0:6:2]
assert( np.array_equal(M,eigenpy.reflex(M,verbose)) );

if verbose: print "===> Block Vector 1x0:6:2 tanspose"
M = Mref[1:2,0:6:2].T
assert( np.array_equal(M,eigenpy.reflex(M,verbose)) );

if verbose: print "===> Block Vector 0:6:2x1"
M = Mref[0:6:2,1:2]
assert( np.array_equal(M,eigenpy.reflex(M,verbose)) );

if verbose: print "===> Block Vector 0:6:2x1 tanspose"
M = Mref[0:6:2,1:2].T
assert( np.array_equal(M,eigenpy.reflex(M,verbose)) );

if verbose: print "===> From Py to Eigen::VectorXd"
if verbose: print "===> From Py to Eigen::VectorXd"
if verbose: print "===> From Py to Eigen::VectorXd"

if verbose: print "===> Block Vector 0:6:2x1 1 dim"
M = Mref[0:6:2,1].T
assert( np.array_equal(np.array([M,]).T,eigenpy.reflexV(M,verbose)) );

if verbose: print "===> Block Vector 0:6:2x1"
M = Mref[0:6:2,1:2]
assert( np.array_equal(M,eigenpy.reflexV(M,verbose)) );

if verbose: print "===> Block Vector 0:6:2x1 transpose"
M = Mref[0:6:2,1:2].T
assert( np.array_equal(M.T,eigenpy.reflexV(M,verbose)) );

if verbose: print "===> From Py to Eigen::Matrix3d"
if verbose: print "===> From Py to Eigen::Matrix3d"
if verbose: print "===> From Py to Eigen::Matrix3d"

if verbose: print "===> Block Vector 0:3x0:6:2 "
M = Mref[0:3,0:6:2]
assert( np.array_equal(M,eigenpy.reflex33(M,verbose)) );

if verbose: print "===> Block Vector 0:3x0:6:2 T"
M = Mref[0:3,0:6].T
try:
    assert( np.array_equal(M,eigenpy.reflex33(M,verbose)) );
except eigenpy.Exception, e:
    if verbose: print "As expected, got the following /ROW/ error:", e.message

if verbose: print "===> From Py to Eigen::Vector3d"
if verbose: print "===> From Py to Eigen::Vector3d"
if verbose: print "===> From Py to Eigen::Vector3d"

M = Mref[0:3,1:2]
assert( np.array_equal(M,eigenpy.reflex3(M,verbose)) );

