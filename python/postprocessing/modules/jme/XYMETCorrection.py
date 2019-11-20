import enum
import ROOT
import math

class RunEra(enum.Enum):
    y2017B = 1
    y2017C = 2
    y2017D = 3
    y2017E = 4
    y2017F = 5
    y2017MC = 6


def METXYCorr_Met_MetPhi(uncormet, uncormet_phi, runnb, year, isMC, npv):
  if npv>100:
    npv=100
  
  runera = None;

  if isMC:
    runera = "y2017MC"
  elif (not isMC and runnb >=297020 and runnb<=299329 ):
    runera = "y2017B"
  elif (not isMC and runnb >=299337 and runnb<=302029 ):
    runera = "y2017C"
  elif (not isMC and runnb >=302030 and runnb<=303434 ):
    runera = "y2017D"
  elif (not isMC and runnb >=303435 and runnb<=304826 ):
    runera = "y2017E"
  elif (not isMC and runnb >=304911 and runnb<=306462 ):
    runera = "y2017F"
  
  METxcorr = 0
  METycorr = 0

  if(runera=="y2017B") :
    METxcorr = -(-0.19563*npv +1.51859)
  if(runera=="y2017B") :
    METycorr = -(0.306987*npv +-1.84713)
  if(runera=="y2017C") :
    METxcorr = -(-0.161661*npv +0.589933)
  if(runera=="y2017C") :
    METycorr = -(0.233569*npv +-0.995546)
  if(runera=="y2017D") :
    METxcorr = -(-0.180911*npv +1.23553)
  if(runera=="y2017D") :
    METycorr = -(0.240155*npv +-1.27449)
  if(runera=="y2017E") :
    METxcorr = -(-0.149494*npv +0.901305)
  if(runera=="y2017E") :
    METycorr = -(0.178212*npv +-0.535537)
  if(runera=="y2017F") :
    METxcorr = -(-0.165154*npv +1.02018)
  if(runera=="y2017F") :
    METycorr = -(0.253794*npv +0.75776)
  if(runera=="y2017MC"):
    METxcorr = -(-0.182569*npv +0.276542)
  if(runera=="y2017MC"):
    METycorr = -(0.155652*npv +-0.417633)
  

  CorrectedMET_x = uncormet *math.cos( uncormet_phi)+METxcorr
  CorrectedMET_y = uncormet *math.sin( uncormet_phi)+METycorr

  CorrectedMET = math.sqrt(CorrectedMET_x*CorrectedMET_x+CorrectedMET_y*CorrectedMET_y)
  CorrectedMETPhi = 0
  if(CorrectedMET_x==0 and CorrectedMET_y>0):
    CorrectedMETPhi = ROOT.TMath.Pi()
  elif(CorrectedMET_x==0 and CorrectedMET_y<0 ):
    CorrectedMETPhi = -ROOT.TMath.Pi()
  elif(CorrectedMET_x >0):
    CorrectedMETPhi = ROOT.TMath.ATan(CorrectedMET_y/CorrectedMET_x)
  elif(CorrectedMET_x <0 and CorrectedMET_y>0):
    CorrectedMETPhi = ROOT.TMath.ATan(CorrectedMET_y/CorrectedMET_x) + ROOT.TMath.Pi()
  elif(CorrectedMET_x <0 and CorrectedMET_y<0):
    CorrectedMETPhi = ROOT.TMath.ATan(CorrectedMET_y/CorrectedMET_x) - ROOT.TMath.Pi()
  else:
    CorrectedMETPhi =0


  return CorrectedMET, CorrectedMETPhi

