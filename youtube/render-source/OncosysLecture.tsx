import React from 'react';
import {AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate} from 'remotion';
import {z} from 'zod';
import {useLato} from '../tokens/lato';
import {OncosysProcess} from './OncosysProcess';

// Project-specific, truthful promotional bookends. No fabricated app output.
export const oncosysLectureSchema=z.object({
  mode:z.enum(['open','idea','definitions','recap','prompt','outro']),
  title:z.string(), team:z.string().default(''), lines:z.array(z.string()).default([]),
  labels:z.array(z.string()).default(['Data','Checks','Evidence']),
  credit:z.string().default('Northeastern SEIS'),
  logos:z.array(z.string()).default([]), durationSeconds:z.number().default(10),
});
type Props=z.infer<typeof oncosysLectureSchema>;
export const OncosysLecture:React.FC<Props>=({mode,title,team,lines,labels,credit,logos})=>{
  useLato();const frame=useCurrentFrame();const {durationInFrames}=useVideoConfig();
  const t=frame/durationInFrames;
  const reveal=(i:number)=>interpolate(t,[.05+i*.12,.11+i*.12],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
  const credits=<div style={{position:'absolute',left:120,right:120,bottom:85,display:'flex',alignItems:'center',justifyContent:'space-between',gap:18}}>
    <div style={{fontSize:38,lineHeight:1.4,width:550,flexShrink:0}}>The Open Accelerator (TOA)<br/>OncoSys AI<br/>{credit}<br/>Red Hat</div>
    {logos.map((logo)=><Img key={logo} src={staticFile(logo)} style={{width:logo.includes('red-hat')?220:160,height:180,objectFit:'contain',flexShrink:0}}/>)}
    <Img src={staticFile('northeastern/official/primary-logo-red-black.svg')} style={{width:230,height:110,objectFit:'contain',flexShrink:0}}/>
  </div>;
  const process=<div className="oncosys-opening-animation" style={{position:'absolute',left:880,top:150,width:920,height:620,overflow:'hidden'}}>
    <style>{'.oncosys-opening-animation svg text {display:none}'}</style>
    <div style={{position:'absolute',width:1920,height:1080,transform:'scale(.47)',transformOrigin:'top left',top:70}}>
      <OncosysProcess title="" mode="flow" labels={labels} details={[]} note="" durationSeconds={10} gateLabel="" driftLabel="" cues={[.08,.32,.6,.8]} diagramStyle="show-tell-isometric" objectKinds={['document','adapter','monitor']}/>
    </div>
  </div>;
  return <AbsoluteFill style={{background:'#FFFFFF',color:'#000000',fontFamily:'Lato',padding:120}}>
    <div style={{position:'absolute',left:120,top:85,width:125,height:7,background:'#C8102E'}}/>
    {mode==='open'||mode==='outro'?<>
      <div style={{position:'absolute',left:120,top:170,width:760,fontSize:70,lineHeight:1.13}}>{title}</div>
      <div style={{position:'absolute',left:120,top:425,width:760,fontSize:team.length>65?40:46,lineHeight:1.3,whiteSpace:'pre-line'}}>{team}</div>
      <div style={{position:'absolute',left:120,top:635,width:720,fontSize:40,lineHeight:1.3}}>{mode==='open'?'Research prototype: strengths and next steps':'Thank you, participants and sponsors'}</div>
      {mode==='outro'?<div style={{position:'absolute',left:120,top:710,fontSize:40}}>@NikBearBrown</div>:null}{process}{credits}
    </>:<>
      <div style={{fontSize:64,lineHeight:1.15,marginTop:35,maxWidth:1640}}>{title}</div>
      {mode==='idea'?<>{process}<div style={{position:'absolute',left:120,top:340,width:740,fontSize:55,lineHeight:1.35}}>{lines[0]}</div></>:
      <div style={{position:'absolute',left:145,right:145,top:280,display:'flex',flexDirection:'column',gap:mode==='prompt'?25:48}}>
        {lines.map((line,i)=><div key={i} style={{fontSize:mode==='prompt'?44:46,lineHeight:1.35,opacity:mode==='prompt'?1:reveal(i),borderLeft:'5px solid #C8102E',paddingLeft:32}}>{line}</div>)}
      </div>}
      <div style={{position:'absolute',right:120,bottom:75,maxWidth:1350,textAlign:'right',fontSize:40,color:'#545454'}}>{mode==='prompt'?'Suggested prompt · not an executed agent response':'AI Healthcare Hackathon · '+credit}</div>
    </>}
  </AbsoluteFill>;
};
